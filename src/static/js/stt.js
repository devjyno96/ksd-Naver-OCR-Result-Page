let dom = {
    audioFile: null,
    audioButton: null,

    audioResult: null
};

function init() {
    getDomReferences();
    registerListeners();

    //hideLoadingBox();
}

/**
 * dom 객체 레퍼런스를 가져온다.
 */
function getDomReferences() {
    dom.audioFile = document.getElementById("audioFile");
    dom.audioButton = document.getElementById("audioSubmitButton");

    dom.audioResult = document.getElementById("audioResult");

}

/**
 * 이벤트 리스너를 등록한다.
 */
function registerListeners() {
    dom.audioButton.addEventListener("click", onSTTUpload);
}

function onSTTUpload() {
    var formData = new FormData();
    formData.append('uploadFile', dom.audioFile.files);

    $.ajax({
        type: "POST",
        url: "/api/stt",
        data: dom.audioFile.files[0],
        //dataType: 'json',
        processData: false,
        contentType: false,
        //contentType: "application/json",
        success: function (response) {
            // if error has data => show error msg alert
            dom.audioResult.innerHTML = "<p>" + response.result + "</p>"
            
        }
    });
}