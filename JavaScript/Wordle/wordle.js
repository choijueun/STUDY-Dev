$(function(){
    var answer = 'abcde';
    var user_inputs = $('input')
    $('button').click(function(){
        console.log(user_inputs)
        console.log(user_inputs[0].value)
    });
});