$(function(){
    // 한글 정규식 검사
    function kRe(str) {
        const re = /[ㄱ-ㅎㅏ-ㅣ가-힣]/g; 
        if (re.test(str)) {
            return true;
        }else {
            return false;
        }
    }

    var answer = 'abcde';
    var user_inputs = $('input')
    $('.button').click(function(){
        console.log(user_inputs[0].value)
        console.log(kRe(user_inputs[0].value))
    });

    
});