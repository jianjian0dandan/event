function show_geo(){
  this.ajax_method='GET';
}

show_geo.prototype = {
  call_sync_ajax_request:function(url,method,callback) {
    $.ajax({
      url: url,
      type: method,
      dataType:'json',
      async:true,
      success:callback
  });
  },

  geoData: function(data){
       var geo_data=[]
       var index_mode;
      for (var key in data){
        if(key=="week_geo_track"){
          index_mode = 1; //week

        }else if(key=="all_top"){
          index_mode = 2; //month
          var province_data={};
          var cityValue = data.all_top[0][1];
          //console.log(data.all_top[0][1]+"---"+data.all_top[0][0]);
          var cityName=data.all_top[0][0].split("\t");
          //console.log("l--"+cityName[2]);
          province_data['name']=cityName[2];
          province_data['value']= cityValue;
          geo_data.push(province_data);
          //console.log("geo"+geo_data);
        }else{
          index_mode = 3;  //day
        }
      }

      document.getElementById('des_loc').innerHTML=(data.description);


       require(
       [
              'echarts',
              'zrender'
          ],
      function(ec){
      var myChart = echarts.init(document.getElementById('act_map'),'shine');
      var ecConfig = require('echarts/config');
      var zrEvent = require('zrender/tool/event');
      var curIndx = 0;
      var mapType = [
          'china',
          // 23个省
          '广东', '青海', '四川', '海南', '陕西',
          '甘肃', '云南', '湖南', '湖北', '黑龙江',
          '贵州', '山东', '江西', '河南', '河北',
          '山西', '安徽', '福建', '浙江', '江苏',
          '吉林', '辽宁', '台湾',
          // 5个自治区
          '新疆', '广西', '宁夏', '内蒙古', '西藏',
          // 4个直辖市
          '北京', '天津', '上海', '重庆',
          // 2个特别行政区
          '香港', '澳门'
      ];
    var option = {
      title :{
         subtext:"地理活跃度"
      },
      tooltip : {
          trigger: 'item',
          formatter: '滚轮切换或点击进入该省<br/>{b}:{c}'
      },
      legend: {
          orient: 'vertical',
          x:'right',
          data:['活跃值']
      },
      dataRange: {
          min: 0,
          max: 500,
          color:['orange', 'yellow'],    //'#E0022B', '#E09107'
          text:['高','中','低'],           // 文本，默认为数值文本
          calculable : true
      },
      series : [
          {
              name: '活跃值',
              type: 'map',
              mapType: 'china',
              selectedMode : 'single',
              itemStyle:{
                  normal:{label:{show:true}},
                  emphasis:{label:{show:true}}
              },
              data:geo_data
          }
      ]
  };

        myChart.setOption(option);
  })
}

}

var show_geo = new show_geo();
var uid = 1640601392;
geo_load();
//加载
function geo_load(){
    click_action_geo();
    var geo_url = ' /attribute/location/?uid='+uid+'&time_type=month';
    show_geo.call_sync_ajax_request(geo_url, show_geo.ajax_method, show_geo.geoData);
}

//模式选择
function click_action_geo(){
    $('#mychoice_geo').on('click','input[name="choose_module_geo"]', function(){             
      var index = $('input[name="choose_module_geo"]:checked').val();
      //console.log(index);
      if(index == 1){
        var geo_url = '/attribute/location/?uid='+uid+'&time_type=month';
        show_geo.call_sync_ajax_request(geo_url, show_geo.ajax_method, show_geo.geoData);
      }
      else if(index == 2){
        var geo_url = '/attribute/location/?uid='+uid+'&time_type=week';
        show_geo.call_sync_ajax_request(geo_url, show_geo.ajax_method, show_geo.geoData);    
      }else{
        var geo_url = '/attribute/location/?uid='+uid+'&time_type=day';
        show_geo.call_sync_ajax_request(geo_url, show_geo.ajax_method, show_geo.geoData); 
      }
          //console.log("geo_url"+geo_url);

    });

}
