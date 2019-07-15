const width = 28;
const height = 28;

const MODEL_URL = 'http://59.110.42.211:8887/mnist/model.json' // 
var loadModel = (async function() {
    window.model = await tf.loadLayersModel(MODEL_URL);
    console.log('load model')
    return model;
})
loadModel().then();
var load_img = function(img) {
    let tensor = tf.browser.fromPixels(img)
        .resizeNearestNeighbor([width, height])
//         .resizeBilinear([width, height])
        .mean(2)
        .expandDims()
        .toFloat()
    return tensor.div(255.0);
};
var predict = async function(id) {
    var model = window.model;
    var canvas = document.getElementById(id);
    var example = this.load_img(canvas);
    let prediction = await model.predict(example).data();
    // console.log(prediction)
    let results = Array.from(prediction);
//     console.log(results);
    return results
}