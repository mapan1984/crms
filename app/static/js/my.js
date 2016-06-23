/*
    var st = $('#spend_time');
    var h = st.text()[0];
    var m = st.text().substring(2,4)
    var s = st.text().substring(5,7)
    function startTime(){
        if(s >= 10){
            s = s + 1;
        }else{
            s = parseInt(s[1]) + 1;
        }
        if(s === 60){
            s = 0;
            m = m + 1;
        }
        if(m === 60){
            m = 0;
            h = h + 1;
        }
        st.text(h+":"+m+":"+s)
        t=setTimeout('startTime()',500)
    }
    startTime();
*/
