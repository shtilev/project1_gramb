$((function(){function t(){$(window).scrollTop();var t=0;$("#wpadminbar").length>0&&(t=parseInt($("#wpadminbar").height()));parseInt($("#menutopped").offset().top),$(window).width()}$(window).on("scroll",(function(){t()})),$(window).on("resize",(function(){t()})),$(window).on("load",(function(){t()})),$(".js_menu li").hover((function(){$(this).find("ul:first").show("drop")}),(function(){$(this).find("ul:first").stop(!0,!0).hide("drop")})),$(".js_menu li a").on("click",(function(){if("#"==$(this).attr("href"))return!1})),$(".tabhome").each((function(){$(this).find("a.onehrine:first").addClass("first"),$(this).find("a.onehrine:last").addClass("last")})),$("table").each((function(){$(this).find("th:first").addClass("th1"),$(this).find("th:last").addClass("th2"),$(this).find("tr:last").find("td:first").addClass("td1"),$(this).find("tr:last").find("td:last").addClass("td2")})),$(document).on("click",".checkbox",(function(){$(this).hasClass("act")?($(this).removeClass("act"),$(this).find("input").prop("checked",!1)):($(this).addClass("act"),$(this).find("input").prop("checked",!0))}))}));