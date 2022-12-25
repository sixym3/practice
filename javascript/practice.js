//document.getElementById("demo").innerHTML = "changed by script";

function test_btn_click() {
    document.getElementById("demo").innerHTML = "changed by button";
}

function change_btn_click() {
    let test_btn = document.getElementById("test_btn");
    if (test_btn.disabled) {
        test_btn.innerHTML = "Test";
        test_btn.disabled = false;
    } else {
        test_btn.innerHTML = "Disabled";
        test_btn.disabled = true;
    }
}

let x, y, z;
const a = 10;
var b = "changeable"; //BAD

function getKey(k) {
    return `a key named ${k}`;
}

const obj = {
    id: 5,
    name: "test",
    [getKey('enabled')]: true
}

console.log(Object.getOwnPropertyNames(obj));