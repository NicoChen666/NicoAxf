$(function () {
    // 为发送验证码按钮添加点击事件
    $("#smsBtn").bind("click", function () {
        var data = {
            //得到输入框的手机号
            "phone": $("#phone").val()
        };
        $.ajax({
            //跳到发送验证码路由，将手机号传给request对象
            url: "/verifyCode/",
            // 第一个data是要发送给后台的数据key值，第二个date是数据的键值：{"phone": $("#phone").val()}
            data: data,
            method: "get",
            success: function (data,status) {
                //成功的话在前端打印一下看看验证吗
                // console.log(data);//data 是由views中{"error": 0, "data": {"verifyCode": rand_str}}
                console.log(data.data); //第二个data的具体{"verifyCode": rand_str}
                // console.log(status);
            }
        })
    })
});