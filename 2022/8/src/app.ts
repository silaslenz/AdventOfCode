import "@babylonjs/core/Debug/debugLayer";
import "@babylonjs/inspector";
import {
    Engine,
    Scene,
    Vector3,
    HemisphericLight,
    Mesh,
    MeshBuilder,
    FreeCamera, SceneLoader, Color3, StandardMaterial, PointLight
} from "@babylonjs/core";
import input from './input?raw';


class App {
    transpose(a) {
        return Object.keys(a[0]).map(function (c) {
            return a.map(function (r) {
                return r[c];
            });
        });
    }

    view_length(tree, view) {
        var view_length = 0
        for (let v of view) {
            view_length += 1
            if (v >= tree) {
                break
            }
        }
        return view_length
    }


    constructor() {
        let tree;
        let j;
        let i;
// create the canvas html element and attach it to the webpage
        var canvas = document.createElement("canvas");
        canvas.style.width = "100%";
        canvas.style.height = "100%";
        canvas.id = "gameCanvas";
        document.body.appendChild(canvas);

        // initialize babylon scene and engine
        let engine = new Engine(canvas, true);
        let scene = new Scene(engine);
        scene.ambientColor = new Color3(0.3, 0.3, 0.3);
        let maxheight = 0;
        let maxx = 0;
        let maxz = 0;
        const lines = input.split('\r\n');
        const visibleTrees = new StandardMaterial("myMaterial", scene);
        visibleTrees.ambientColor = new Color3(0, 1, 0);
        const forest = Array.from(Array(lines.length), _ => Array(lines[0].length).fill(0));
        for (let x = 0; x < lines.length; x++) {
            for (let z = 0; z < lines[x].length; z++) {
                forest[x][z] = parseInt(lines[x][z])


            }
        }
        let forest_transposed = this.transpose(forest);

        let visible = 0;
        for (i = 0; i < lines.length; i++) {
            for (j = 0; j < lines[i].length; j++) {
                let height = forest[i][j];
                maxheight = Math.max(maxheight, height);
                maxx = Math.max(maxx, i);
                maxz = Math.max(maxz, j);

                if (height === 0) {
                    tree = MeshBuilder.CreateSphere("sphere", {diameter: 0.5}, scene);
                } else {
                    tree = MeshBuilder.CreateCylinder("tree", {diameter: 0.5, height: height}, scene);
                }
                tree.position.z = j;
                tree.position.x = i;
                tree.position.y = height / 2;
                if (forest[i].slice(0, j).every(val => val < height)
                    || forest[i].slice(j + 1, forest[j].length).every(val => val < height)
                    || forest_transposed[j].slice(0, i).every(val => val < height)
                    || forest_transposed[j].slice(i + 1, forest_transposed[j].length).every(val => val < height)
                ) {
                    tree.material = visibleTrees;
                    visible += 1
                }
            }
        }
        console.log("Part 1: ", visible)

        const ground: Mesh = MeshBuilder.CreateGround("ground", {width: maxx, height: maxz}, scene);
        ground.position.x = maxx / 2;
        ground.position.z = maxz / 2;
        let light = new HemisphericLight("light1", new Vector3(1,1,0), scene);



        const camera: FreeCamera = new FreeCamera("Camera", new Vector3(maxx / 2, maxheight, maxz + 5), scene);
        camera.setTarget(new Vector3(maxx / 2, 0, maxz / 2));
        camera.attachControl(canvas, true);

        // Part 2
        let max = 0;

        for (i = 0; i < lines.length; i++) {
            for (j = 0; j < lines[i].length; j++) {
                let height = forest[i][j];
                let s1 = this.view_length(height, forest[i].slice(0, j).reverse())
                let s2 = this.view_length(height, forest[i].slice(j + 1, forest[i].length))
                let s3 = this.view_length(height, forest_transposed[j].slice(0, i).reverse())
                let s4 = this.view_length(height, forest_transposed[j].slice(i + 1, forest_transposed[j].length))
                let score = s1 * s2 * s3 * s4

                if (score > max) {
                    max = score
                }
            }
        }
        console.log("Part 2: ", max)
        // run the main render loop
        engine.runRenderLoop(() => {
            scene.render();
        });
    }
}

new App();