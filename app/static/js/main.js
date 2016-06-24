$(document).ready(function() {
    var st = $('td.spend_time');
    var h = st.text()[0];
    var m = st.text().substring(2,4);
    var s = st.text().substring(5,7);
    h = parseInt(h)
    s = parseInt(s)
    m = parseInt(m)
    setInterval(function(){
        if(s < 10 && m < 10){
            st.text(h+':0'+m+':0'+s);
        }else if(s < 10){
            st.text(h+':'+m+':0'+s);
        }else{
            st.text(h+':0'+m+':'+s);
        }
        s = s + 1;
        if(s == 60){
            s = 0;
            m = m + 1;
        }
        if(m == 60){
            m = 0;
            h = h +1;
        }
    },1000);
});
