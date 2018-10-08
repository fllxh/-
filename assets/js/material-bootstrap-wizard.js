/*!

 =========================================================
 * Material Bootstrap Wizard - v1.0.2
 =========================================================
 
 * Product Page: https://www.creative-tim.com/product/material-bootstrap-wizard
 * Copyright 2017 Creative Tim (#)
 * Licensed under MIT (https://github.com/creativetimofficial/material-bootstrap-wizard/blob/master/LICENSE.md)
 
 =========================================================
 
 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 */

// Material Bootstrap Wizard Functions

var searchVisible = 0;
var transparent = true;
var mobile_device = false;

$(document).ready(function () {

    $.material.init();

    /*  Activate the tooltips      */
    $('[rel="tooltip"]').tooltip();

    // Code for the Validator
    var $validator = $('.wizard-card form').validate({
        rules: {
            firstname: {
                required: true,
                minlength: 3
            },
            lastname: {
                required: true,
                minlength: 3
            },
            email: {
                required: true,
                minlength: 3,
            }
        },

        errorPlacement: function (error, element) {
            $(element).parent('div').addClass('has-error');
        }
    });

    // Wizard Initialization
    $('.wizard-card').bootstrapWizard({
        'tabClass': 'nav nav-pills',
        'nextSelector': '.btn-next',
        'previousSelector': '.btn-previous',

        onNext: function (tab, navigation, index) {
            var $valid = $('.wizard-card form').valid();
            if (!$valid) {
                $validator.focusInvalid();
                return false;
            }
        },

        onInit: function (tab, navigation, index) {
            //check number of tabs and fill the entire row
            var $total = navigation.find('li').length;
            var $wizard = navigation.closest('.wizard-card');

            $first_li = navigation.find('li:first-child a').html();
            $moving_div = $('<div class="moving-tab">' + $first_li + '</div>');
            $('.wizard-card .wizard-navigation').append($moving_div);

            refreshAnimation($wizard, index);

            $('.moving-tab').css('transition', 'transform 0s');
        },

        onTabClick: function (tab, navigation, index) {
            var $valid = $('.wizard-card form').valid();

            if (!$valid) {
                return false;
            } else {
                return true;
            }
        },

        onTabShow: function (tab, navigation, index) {
            var $total = navigation.find('li').length;
            var $current = index + 1;

            var $wizard = navigation.closest('.wizard-card');

            // If it's the last tab then hide the last button and show the finish instead
            if ($current >= $total) {
                $($wizard).find('.btn-next').hide();
                $($wizard).find('.btn-finish').show();
            } else {
                $($wizard).find('.btn-next').show();
                $($wizard).find('.btn-finish').hide();
            }

            button_text = navigation.find('li:nth-child(' + $current + ') a').html();

            setTimeout(function () {
                $('.moving-tab').text(button_text);
            }, 150);

            var checkbox = $('.footer-checkbox');

            if (!index == 0) {
                $(checkbox).css({
                    'opacity': '0',
                    'visibility': 'hidden',
                    'position': 'absolute'
                });
            } else {
                $(checkbox).css({
                    'opacity': '1',
                    'visibility': 'visible'
                });
            }

            refreshAnimation($wizard, index);
        }
    });


    // Prepare the preview for profile picture
    $("#wizard-picture").change(function () {
        readURL(this);
    });

    $('[data-toggle="wizard-radio"]').click(function () {
        wizard = $(this).closest('.wizard-card');
        wizard.find('[data-toggle="wizard-radio"]').removeClass('active');
        $(this).addClass('active');
        $(wizard).find('[type="radio"]').removeAttr('checked');
        $(this).find('[type="radio"]').attr('checked', 'true');
    });

    $('[data-toggle="wizard-checkbox"]').click(function () {
        if ($(this).hasClass('active')) {
            $(this).removeClass('active');
            $(this).find('[type="checkbox"]').removeAttr('checked');
        } else {
            $(this).addClass('active');
            $(this).find('[type="checkbox"]').attr('checked', 'true');
        }
    });

    $('.set-full-height').css('height', 'auto');

});


//Function to show image before upload

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#wizardPicturePreview').attr('src', e.target.result).fadeIn('slow');
        }
        reader.readAsDataURL(input.files[0]);
    }
}

$(window).resize(function () {
    $('.wizard-card').each(function () {
        $wizard = $(this);

        index = $wizard.bootstrapWizard('currentIndex');
        refreshAnimation($wizard, index);

        $('.moving-tab').css({
            'transition': 'transform 0s'
        });
    });
});

function refreshAnimation($wizard, index) {
    $total = $wizard.find('.nav li').length;
    $li_width = 100 / $total;

    total_steps = $wizard.find('.nav li').length;
    move_distance = $wizard.width() / total_steps;
    index_temp = index;
    vertical_level = 0;

    mobile_device = $(document).width() < 600 && $total > 3;

    if (mobile_device) {
        move_distance = $wizard.width() / 2;
        index_temp = index % 2;
        $li_width = 50;
    }

    $wizard.find('.nav li').css('width', $li_width + '%');

    step_width = move_distance;
    move_distance = move_distance * index_temp;

    $current = index + 1;

    if ($current == 1 || (mobile_device == true && (index % 2 == 0))) {
        move_distance -= 8;
    } else if ($current == total_steps || (mobile_device == true && (index % 2 == 1))) {
        move_distance += 8;
    }

    if (mobile_device) {
        vertical_level = parseInt(index / 2);
        vertical_level = vertical_level * 38;
    }

    $wizard.find('.moving-tab').css('width', step_width);
    $('.moving-tab').css({
        'transform': 'translate3d(' + move_distance + 'px, ' + vertical_level + 'px, 0)',
        'transition': 'all 0.5s cubic-bezier(0.29, 1.42, 0.79, 1)'

    });
}

materialDesign = {

    checkScrollForTransparentNavbar: debounce(function () {
        if ($(document).scrollTop() > 260) {
            if (transparent) {
                transparent = false;
                $('.navbar-color-on-scroll').removeClass('navbar-transparent');
            }
        } else {
            if (!transparent) {
                transparent = true;
                $('.navbar-color-on-scroll').addClass('navbar-transparent');
            }
        }
    }, 17)

}

function debounce(func, wait, immediate) {
    var timeout;
    return function () {
        var context = this, args = arguments;
        clearTimeout(timeout);
        timeout = setTimeout(function () {
            timeout = null;
            if (!immediate) func.apply(context, args);
        }, wait);
        if (immediate && !timeout) func.apply(context, args);
    };
}

$(function () {
//先选出 textarea 和 统计字数 dom 节点
    var wordCount = $("#wordCount"),
        textArea = wordCount.find("textarea"),
        word = wordCount.find(".word");
//调用
    statInputNum(textArea, word);
    var wordCount1 = $("#wordCount1"),
        textArea1 = wordCount1.find("textarea"),
        word1 = wordCount1.find(".word");
//调用
    statInputNum(textArea1, word1);
});

function statInputNum(textArea, numItem) {
    var max = numItem.text(),
        curLength;
    curLength = textArea.val().length;
    numItem.text(max - curLength);
    textArea.on('input propertychange', function () {
        var curComNum = $(this).val().length - $(this).val().replace(/[\ |\，|\。|\！|\？|\：|\￥|\%|\、|\“|\”|\（|\）|\；\-|\_|\+|\=|\||\\|\[|\]|\{|\}|\;|\:|\"|\'|\,|\<|\.|\>|\/|\?]/g, "")
            .length;
        textArea[0].setAttribute("maxlength", parseInt(max) + parseInt(curComNum));
        if (max - $(this).val().length + curComNum < 0)
            numItem.text(0);
        else
            numItem.text(max - $(this).val().length + curComNum);
    });
}

document.onkeydown = function (evt) {
    var isie = (document.all) ? true : false;
    var key;
    var srcobj;
    // if the agent is an IE browser, it's easy to do this.
    if (isie) {
        key = event.keyCode;
        srcobj = event.srcElement;
    }
    else {
        key = evt.which;
        srcobj = evt.target;
    }
    if (key == 13 && srcobj.type != 'button' && srcobj.type != 'submit' && srcobj.type != 'reset' && srcobj.type != 'textarea' && srcobj.type != '') {
        setTimeout(function () {
            if (isie)
                event.keyCode = 9;
            else {
                var el = getNextElement(evt.target);
                if (el.type != 'hidden')
                    ;   //nothing to do here.
                else
                    while (el.type == 'hidden')
                        el = getNextElement(el);
                if (!el)
                    return false;
                else
                    el.focus();

                //把提交按钮retrun 为false
                return false;
            }
        }, 0);
        e.preventDefault ? e.preventDefault() : (e.returnValue = false);

    }
}

function getNextElement(field) {
    var form = field.form;
    for (var e = 0; e < form.elements.length; e++) {
        if (field == form.elements[e])
            break;
    }
    return form.elements[++e % form.elements.length];
}

function testid(id) {

    var format = /^(([1][1-5])|([2][1-3])|([3][1-7])|([4][1-6])|([5][0-4])|([6][1-5])|([7][1])|([8][1-2]))\d{4}(([1][9]\d{2})|([2]\d{3}))(([0][1-9])|([1][0-2]))(([0][1-9])|([1-2][0-9])|([3][0-1]))\d{3}[0-9xX]$/;
    //号码规则校验
    if (!format.test(id)) {
        return {'status': 0, 'msg': '身份证号码不合规'};
    }
    //区位码校验
    //出生年月日校验   前正则限制起始年份为1900;
    var year = id.substr(6, 4),//身份证年
        month = id.substr(10, 2),//身份证月
        date = id.substr(12, 2),//身份证日
        time = Date.parse(month + '-' + date + '-' + year),//身份证日期时间戳date
        now_time = Date.parse(new Date()),//当前时间戳
        dates = (new Date(year, month, 0)).getDate();//身份证当月天数
    if (time > now_time || date > dates) {
        return {'status': 0, 'msg': '出生日期不合规'}
    }
    //校验码判断
    var c = new Array(7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2);   //系数
    var b = new Array('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2');  //校验码对照表
    var id_array = id.split("");
    var sum = 0;
    for (var k = 0; k < 17; k++) {
        sum += parseInt(id_array[k]) * parseInt(c[k]);
    }
    if (id_array[17].toUpperCase() != b[sum % 11].toUpperCase()) {
        return {'status': 0, 'msg': '身份证校验码不合规'}
    }
    return {'status': 1, 'msg': '校验通过'}
}

//判断字符是否为空的方法
function isEmpty(obj) {
    if (typeof obj == "undefined" || obj == null || obj == "") {
        return true;
    } else {
        return false;
    }
}

function checkdata() {
    var pass = true
    var stu_id = document.getElementsByName("stu_id")[0].value;
    identify_id = testid(stu_id);
    if (identify_id.status) {
        pass = true;
    }
    else {
        alert(identify_id.msg + '请检查后重试!');
        pass = false;
    }

    var stu_sno = document.getElementsByName("stu_sno")[0].value;
    if (stu_sno.length != 12) {
        alert('学号位数有误，请修改后重试!');
        pass = false;
    }

    var stu_tel = document.getElementsByName("stu_tel")[0].value;
    if (stu_tel.length != 11) {
        alert('手机号位数需要为11位，请修改后重试!');
        pass = false;
    }

    var stu_p1 = document.getElementsByName("stu_p1")[0].value;
    var stu_p2 = document.getElementsByName("stu_p2")[0].value;
    var stu_p3 = document.getElementsByName("stu_p3")[0].value;
    var stu_p4 = document.getElementsByName("stu_p4")[0].value;
    if (stu_sno.substr(0, 4) != '2017' && (isEmpty(stu_p3) || isEmpty(stu_p4))) {
        alert('请填写综合测评成绩，请修改后重试!');
        pass = false;
    }
    else if (stu_sno.substr(0, 4) != '2017' && stu_p2 != stu_p4) {
        alert('成绩排名和综合测评总人数不一致，请修改后重试!');
        pass = false;
    }
    if (stu_sno.substr(0, 4) == '2017' && !(isEmpty(stu_p3) && isEmpty(stu_p4))) {
        alert('请不要填写综合测评成绩，请修改后重试!');
        pass = false;
    }

    var stu_reason1 = document.getElementsByName("stu_reason1")[0].value;
    if (stu_reason1.length < 190) {
        alert('申请理由字数需要大于190，请修改后重试!');
        pass = false;
    }

    var stu_reason2 = document.getElementsByName("stu_reason2")[0].value;
    if (stu_reason2.length < 90) {
        alert('推荐理由字数需要大于90，请修改后重试!');
        pass = false;
    }
    if (pass == true) {
        alert('已成功提交，请下载你的申请表。\nε=ε=ε=ε=ε=ε=┌(;￣◇￣)┘');
    }
    return pass;

}
;


