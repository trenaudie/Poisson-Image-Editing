

document.querySelector("#bird").onclick = function () {
    eel.source_bird()(function () {
        document.querySelector(".choice1").innerHTML = "Choice : bird";
    })
}

document.querySelector("#shark").onclick = function () {
    eel.source_shark()(function () {
        document.querySelector(".choice1").innerHTML = "Choice : shark";
    })
}

document.querySelector("#objets").onclick = function () {
    eel.source_objets()(function () {
        document.querySelector(".choice1").innerHTML = "Choice : objects";
    })
}

document.querySelector("#statue").onclick = function () {
    eel.source_statue()(function () {
        document.querySelector(".choice1").innerHTML = "Choice : statue";
    })
}

document.querySelector("#forest").onclick = function () {
    eel.target_forest()(function () {
        document.querySelector(".choice2").innerHTML = "Choice : Forest";
    })
}

document.querySelector("#ocean").onclick = function () {
    eel.target_ocean()(function () {
        document.querySelector(".choice2").innerHTML = "Choice : Ocean";
    })
}

document.querySelector("#sky").onclick = function () {
    eel.target_sky()(function () {
        document.querySelector(".choice2").innerHTML = "Choice : sky";
    })
}

document.querySelector("#min").onclick = function () {
    eel.algo_min()(function () {
        document.querySelector(".choice3").innerHTML = "Choice : erase";
        
    })
}

document.querySelector("#max").onclick = function () {
    eel.algo_max()(function () {
        document.querySelector(".choice3").innerHTML = "Choice : insert";
    })
}




document.querySelector("#run").onclick = function () {
    eel.run()(function () {
    })
}