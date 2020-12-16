/*
{
    "베일리_1": 5127,
    "wcst": 5126,
    "vineland": 5125,
    "stroop_1": 5124,
    "SMS_1": 5123,
    "LEITER_3": 5122,
    "LEITER_2": 5120,
    "LEITER_1": 5118,
    "Leiter": 5117,
    "GROSS_1": 5115,
    "CAT": 5114,
    "CARS_서울성모형식": 5113,
    "bayley": 5103,
    "ADI_R": 5102,
    "ABC_4": 5101,
    "ABC_3": 5100,
    "ABC_2": 5098,
    "ABC_1": 5097,
    "척도3": 5028,
    "척도2": 5027,
    "척도1": 5026,
    "특수뇌파 판독지": 4400,
    "처방약물": 4399,
    "소변검사판독지": 4398,
    "MRI 판독지": 4397,
    "CAT 결과표": 4396,
    "혈액검사2": 4301,
    "WISC": 4299,
    "처방 약물": 4294,
    "WPPSI": 4292
}

*/

var templateToFunction = {
    5127 : template5127,
    5126 : template5126,
    5125 : template5125,
    5124 : template5124,
    5123 : template5123,
    5122 : template5122,
    5120 : template5120,
    5118 : template5118,
    5117 : template5117,
    5115 : template5115,
    5114 : template5114,
    5113 : template5113,
    5103 : template5103,
    5102 : template5102,
    5101 : template5101,
    5100 : template5100,
    5098 : template5098,
    5097 : template5097,
    5028 : template5028,
    5027 : template5027,
    5026 : template5026,
    4400 : template4400,
    4399 : template4399,
    4398 : template4398,
    4397 : template4397,
    4396 : template4396,
    4301 : template4301,
    4299 : template4299,
    4294 : template4294,
    4292 : template4292
}


function ocrFilter(response){
    var result = templateToFunction[Number(response.images[0].matchedTemplate.id)](response.images[0].fields);
    
    if (result == null){
        var resultStr = "<h1>" + response.images[0].matchedTemplate.id + " Result table is not ready.</h1>"
        return new DOMParser().parseFromString(resultStr, "text/html").body;
    }
    else{     
        var doc = new DOMParser().parseFromString(result, "text/html");
        return doc.body;
    }
}


function template5127(result){
    var resultStr = "<table style='border : 1px solid #444444'>\
            <tr style='background-color: skyblue;'>\
                <th>발달검사</th><th>척도(합산)점수</th><th>발달지수</th><th>백분위</th><th>신뢰구간(95%)</th>\
            </tr>\
            <tr>\
                <th>인지</th><th>" + result[0].inferText +"</th><th>" + result[1].inferText +"</th><th>" + result[2].inferText + "</th><th>" + result[3].inferText + "</th>\
            </tr>\
            <tr>\
                <th>언어</th><th>" + result[4].inferText +"</th><th>" + result[5].inferText +"</th><th>" + result[6].inferText + "</th><th>" + result[7].inferText + "</th>\
            </tr>\
            <tr>\
                <th>운동</th><th>" + result[8].inferText +"</th><th>" + result[9].inferText +"</th><th>" + result[10].inferText + "</th><th>" + result[11].inferText + "</th>\
            </tr>\
            <tr>\
                <th>사회-정서</th><th>" + result[12].inferText +"</th><th>" + result[13].inferText +"</th><th>" + result[14].inferText + "</th><th>" + result[15].inferText + "</th>\
            </tr>\
            <tr>\
                <th>적응행동</th><th>" + result[16].inferText +"</th><th>" + result[17].inferText +"</th><th>" + result[18].inferText + "</th><th>" + result[19].inferText + "</th>\
            </tr>\
        </table>";
    return resultStr

}


function template5126(response){

}


function template5125(response){

}


function template5124(response){

}


function template5123(response){

}


function template5122(response){

}


function template5120(response){

}


function template5118(response){

}


function template5117(response){

}


function template5115(response){

}


function template5114(response){

}


function template5113(response){

}


function template5103(response){

}


function template5102(response){

}


function template5101(response){

}


function template5100(response){

}


function template5098(response){

}


function template5097(response){

}


function template5028(response){

}


function template5027(response){

}


function template5026(response){

}


function template4400(response){

}


function template4399(response){

}


function template4398(response){

}


function template4397(response){

}


function template4396(response){

}


function template4301(response){

}


function template4299(response){

}


function template4294(response){

}


function template4292(response){

}