let dom = {
    ocrImage: null,
    ocrUploadButton: null,
    ocrImageOutput: null,

    ocrResultTable: null,
    ocrResultRow: null,

    loadingBox: null
};

var jsonViewer = new JSONViewer();
document.querySelector("#json").appendChild(jsonViewer.getContainer());


function init() {
    getDomReferences();
    registerListeners();

    //hideLoadingBox();
}

/**
 * dom 객체 레퍼런스를 가져온다.
 */
function getDomReferences() {
    dom.ocrImage = document.getElementById("imageFile");
    dom.ocrUploadButton = document.getElementById("imageSubmitButton");
    dom.ocrImageOutput = document.getElementById("imageShowOutput");

    dom.ocrResultTable = document.getElementById("rightTable");
    dom.ocrResultRow = document.getElementById("rightRow");

    dom.loadingBox = document.getElementById("loadingBox");
}

/**
 * 이벤트 리스너를 등록한다.
 */
function registerListeners() {
    dom.ocrUploadButton.addEventListener("click", onOcrUpload);
    dom.ocrImage.addEventListener("change", ImageShow);
}

function ImageShow(event) {
    var reader = new FileReader();
    reader.onload = function(){
      dom.ocrImageOutput.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
  };

function onOcrUpload() {
    var formData = new FormData();
    formData.append('uploadFile', dom.ocrImage.files[0]);

    $.ajax({
        type: "POST",
        url: "/api/ocr-requests",
        data: dom.ocrImage.files[0],
        dataType: 'json',
        processData: false,
        contentType: false,
        //contentType: "application/json",
        success: function (response) {
            // if error has data => show error msg alert
            while(dom.ocrResultTable.lastChild){
            dom.ocrResultTable.removeChild(dom.ocrResultTable.lastChild);
            }
            dom.ocrResultTable.appendChild(ocrFilter(response));

            jsonViewer.showJSON(response);
        }
    });
}

/*
// loading box function
function showLoadingBox() {
    dom.loadingBox.style.display = "inline-block";
}


function hideLoadingBox() {
    dom.loadingBox.style.display = "none";
}
*/