const width = 28;
const height = 28;
const MODEL_URL = 'http://localhost:5000/models/mnist/model.json' 

var loadModel = (async function() {
    window.model = await tf.loadLayersModel(MODEL_URL);
    console.log('load model')
    return model;
})
loadModel().then();
var load_img = function(img) {
    let tensor = tf.browser.fromPixels(img)
        .resizeNearestNeighbor([width, height])
        .mean(2)
        .expandDims()
        .toFloat()
        .div(255.0)
    return tensor;
};
var predict = async function(id) {
    var model = window.model;
    var canvas = document.getElementById(id);
    var example = this.load_img(canvas);
    let prediction = await model.predict(example).data();
    let results = Array.from(prediction);

    return results
}