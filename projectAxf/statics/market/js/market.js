$(function () {
    var idStr = "yellow" + location.href.split("/")[4];
    // 因为idStr没有在css 中，所以需要用document.getElementById(idStr)
    var $span = $(document.getElementById(idStr));
    $span.addClass("yellow");
    // 点击全部分类,综合排序
    // 因为typeBtn typeBtn 作为id 可以直接用id选择器选择
    // var $typeBtn = $(document.getElementById("typeBtn"));
    // var $sortBtn = $(document.getElementById("typeBtn"));
    // 添加点击事件
    $("#typeBtn").bind("click", function () {
        $("#typeDiv").toggle();
        $("#sortDiv").hide();
    });
    $("#sortBtn").bind("click", function () {
        $("#sortDiv").toggle();
        $("#typeDiv").hide();
    });
    function hideSelf() {
        $(this).hide()
    }
    // 函数的引用不加()
    $("#typeDiv").bind("click",hideSelf);
    $("#sortDiv").bind("click",hideSelf);

    var idType = "type" + location.href.split("/")[5];
    var $typeSpan = $(document.getElementById(idType));
    $typeSpan.addClass("typeSortBackground");
    var idSort = "sort" + location.href.split("/")[6];
    var $sortSpan = $(document.getElementById(idSort));
    $sortSpan.addClass("typeSortBackground");
});
