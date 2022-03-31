$(function(){
    // DRAG UNABLE
    // document.oncontextmenu = function(){ return false; }
    $(document).on('contextmenu dragstart selectstart keydown', function(e){ return false; })

    // REGULAR EXPRESSION
    function kRe(str) {
        // 한글 정규식
        const re = /[ㄱ-ㅎㅏ-ㅣ가-힣]/g; 
        // 검사
        if (re.test(str)) { return true; }
        else { return false; }
    }

    // SHIFT
    function toggleShift(){
        // SHIFT 영역
        let vr_shift = $('.vr-shift')
        // SHIFT 토글
        vr_shift.toggleClass('disabled').toggleClass('inline-block')
    }
    $(document).on( 'click', '#SHIFT', function(){ toggleShift(); } );

    // DELETE
    $(document).on( 'click', '#DELETE', function(){
        console.log('click #DELETE')
    });

    // SUBMIT
    $(document).on( 'click', '#SUBMIT', function(){
        console.log('click #SUBMIT')
    });
});