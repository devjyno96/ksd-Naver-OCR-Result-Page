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
    5127: template5127,
    5126: template5126,
    5125: template5125,
    5124: template5124,
    5123: template5123,
    5122: template5122,
    5120: template5120,
    5118: template5118,
    5117: template5117,
    5115: template5115,
    5114: template5114,
    5113: template5113,
    5103: template5103,
    5102: template5102,
    5101: template5101,
    5100: template5100,
    5098: template5098,
    5097: template5097,
    5028: template5028,
    5027: template5027,
    5026: template5026,
    4400: template4400,
    4399: template4399,
    4398: template4398,
    4397: template4397,
    4396: template4396,
    4301: template4301,
    4299: template4299,
    4294: template4294,
    4292: template4292
}


function ocrFilter(response) {
    var result = templateToFunction[Number(response.images[0].matchedTemplate.id)](response.images[0].fields);

    if (result == null) {
        var resultStr = "<h1>" + response.images[0].matchedTemplate.id + " Result table is not ready.</h1>"
        return new DOMParser().parseFromString(resultStr, "text/html").body;
    }
    else {
        var doc = new DOMParser().parseFromString(result, "text/html");
        return doc.body;
    }
}


function template5127(result) {
    var resultStr = "<table style='border : 1px solid #444444'>\
            <tr style='background-color: skyblue;'>\
                <th>발달검사</th><th>척도(합산)점수</th><th>발달지수</th><th>백분위</th><th>신뢰구간(95%)</th>\
            </tr>\
            <tr>\
                <th>인지</th><th>" + result[0].inferText + "</th><th>" + result[1].inferText + "</th><th>" + result[2].inferText + "</th><th>" + result[3].inferText + "</th>\
            </tr>\
            <tr>\
                <th>언어</th><th>" + result[4].inferText + "</th><th>" + result[5].inferText + "</th><th>" + result[6].inferText + "</th><th>" + result[7].inferText + "</th>\
            </tr>\
            <tr>\
                <th>운동</th><th>" + result[8].inferText + "</th><th>" + result[9].inferText + "</th><th>" + result[10].inferText + "</th><th>" + result[11].inferText + "</th>\
            </tr>\
            <tr>\
                <th>사회-정서</th><th>" + result[12].inferText + "</th><th>" + result[13].inferText + "</th><th>" + result[14].inferText + "</th><th>" + result[15].inferText + "</th>\
            </tr>\
            <tr>\
                <th>적응행동</th><th>" + result[16].inferText + "</th><th>" + result[17].inferText + "</th><th>" + result[18].inferText + "</th><th>" + result[19].inferText + "</th>\
            </tr>\
        </table>";
    return resultStr

}


function template5126(result) {
    var resultStr = `<table style='border : 1px solid #444444'>\
    <tr>\
        <th></th>\
        <th>Trials to Complete Categoryial</th><th>Total Error</th><th>Perseverative Response</th>\
        <th>Perseverative Error</th><th>Non-Perseverative Error</th><th>Maintain Set Failure</th>\
    </tr>\
    <tr>\
        <th>Color</th>\
        <th>${result[0].inferText}</th><th>${result[1].inferText}</th><th>${result[2].inferText}</th>\
        <th>${result[3].inferText}</th><th>${result[4].inferText}</th><th>${result[5].inferText}</th>\
    </tr>\
    <tr>\
        <th>Form</th>\
        <th>${result[6].inferText}</th><th>${result[7].inferText}</th><th>${result[8].inferText}</th>\
        <th>${result[9].inferText}</th><th>${result[10].inferText}</th><th>${result[11].inferText}</th>\
    </tr>\
    <tr>\
        <th>Number</th>\
        <th>${result[12].inferText}</th><th>${result[13].inferText}</th><th>${result[14].inferText}</th>\
        <th>${result[15].inferText}</th><th>${result[16].inferText}</th><th>${result[17].inferText}</th>\
    </tr>\
    <tr>\
        <th>Color</th>\
        <th>${result[18].inferText}</th><th>${result[19].inferText}</th><th>${result[20].inferText}</th>\
        <th>${result[21].inferText}</th><th>${result[22].inferText}</th><th>${result[23].inferText}</th>\
    </tr>\
    <tr>\
        <th>Form</th>\
        <th>${result[24].inferText}</th><th>${result[25].inferText}</th><th>${result[26].inferText}</th>\
        <th>${result[27].inferText}</th><th>${result[28].inferText}</th><th>${result[29].inferText}</th>\
    </tr>\
    <tr>\
        <th>Number</th>\
        <th>${result[30].inferText}</th><th>${result[31].inferText}</th><th>${result[32].inferText}</th>\
        <th>${result[33].inferText}</th><th>${result[34].inferText}</th><th>${result[35].inferText}</th>\
    </tr>\
    <tr>\
        <th>Total</th>\
        <th>${result[36].inferText}</th><th>${result[37].inferText}</th><th>${result[38].inferText}</th>\
        <th>${result[39].inferText}</th><th>${result[40].inferText}</th><th>${result[41].inferText}</th>\
    </tr>\
    <tr>\
        <th colspan="3">Categories Completed</th><th colspan="2">${result[42].inferText}</th>\
        <th colspan="2" rowspan="2">${result[44].inferText}</th>
    </tr>\
    <tr> 
        <th colspan="3">Total Trials</th><th colspan="2">${result[43].inferText}</th>\
    </tr>
</table>`;
    return resultStr
}


function template5125(result) {
    var resultStr = `<table style='border : 1px solid #444444'>\
    <tr>\
        <th colspan="3"  style='background-color: skyblue;'>적응행동조합점수(K-Vineland-II)</th>\<th colspan="2">${result[0].inferText}</th>\
        <th style='background-color: skyblue;'>신뢰구간</th><th>${result[1].inferText}</th>\
        <th style='background-color: skyblue;'>백분위</th><th>${result[2].inferText}</th>\
    </tr>\
    <tr style='background-color: skyblue;'>\
        <th colspan="3">의사 소통</th><th colspan="3">생활 기술</th><th colspan="3">사회성</th>\
    </tr>\
    <tr>\
        <th colspan="3">${result[3].inferText}</th><th colspan="3">${result[3].inferText}</th><th colspan="3">${result[5].inferText}</th>\
    </tr>\
    <tr style='background-color: skyblue;'>\
        <th> 수용 </th><th> 표현 </th><th> 쓰기 </th>\
        <th> 개인 </th><th> 가정 </th><th> 지역사회 </th>\
        <th> 대인관계 </th><th> 놀이여가 </th><th> 대처기술 </th>
    </tr>\
    <tr>\
        <th> ${result[6].inferText} </th><th> ${result[7].inferText} </th><th> ${result[8].inferText} </th>\
        <th> ${result[9].inferText} </th><th> ${result[10].inferText} </th><th> ${result[11].inferText} </th>\
        <th> ${result[12].inferText} </th><th> ${result[13].inferText} </th><th> ${result[14].inferText} </th>
    </tr>\
    <tr>\
        <th colspan="2" style='background-color: skyblue;'> 부적응행동(내현화) </th><th> ${result[15].inferText} </th>\
        <th colspan="2" style='background-color: skyblue;'> 부적응행동(외현화) </th><th> ${result[16].inferText} </th>\
        <th colspan="2" style='background-color: skyblue;'> 결정적 문항 심각도 </th><th> ${result[17].inferText} </th>\
    </tr>\
</table>`
return resultStr
}


function template5124(result) {
    var resultStr = `<table style='border : 1px solid #444444'>\
    <tr style='background-color: skyblue;'>\
        <th>Scale</th><th>Raw Score</th><th>T-score</th>\
    </tr>\
    <tr>\
        <th style='background-color: rgb(254, 255, 153);'>단어 점수<br>(W)</th><th>${result[0].inferText}</th><th>${result[1].inferText}</th>\
    </tr>\
    <tr>\
        <th style='background-color: rgb(254, 255, 153);'>색상 점수<br>( C ))</th><th>${result[2].inferText}</th><th>${result[3].inferText}</th>\
    </tr>\
    <tr>\
        <th style='background-color: rgb(254, 255, 153);'>색상-단어 점수<br>(CW)</th><th>${result[4].inferText}</th><th>${result[5].inferText}</th>\
    </tr>\
    <tr>\
        <th style='background-color: rgb(254, 255, 153);'>간섭 점수<br>(C-CW)</th><th>${result[6].inferText}</th><th>${result[7].inferText}</th>\
    </tr>\
   </table>`
    return resultStr
}


function template5123(result) {

}


function template5122(result) {

}


function template5120(result) {

}


function template5118(result) {

}


function template5117(result) {

}


function template5115(result) {

}


function template5114(result) {

}


function template5113(result) {

}


function template5103(result) {

}


function template5102(result) {

}


function template5101(result) {

}


function template5100(result) {

}


function template5098(result) {

}


function template5097(result) {

}


function template5028(result) {

}


function template5027(result) {

}


function template5026(result) {

}


function template4400(result) {

}


function template4399(result) {

}


function template4398(result) {

}


function template4397(result) {

}


function template4396(result) {

}


function template4301(result) {

}


function template4299(result) {

}


function template4294(result) {

}


function template4292(result) {

}