(function ($, google, undefined) {
    $(document).ready(function () {
        //gapi.client.setApiKey('AIzaSyAOcFq0wke1o0OB1c_CdyrIiaZxClEuLZ4');
        google.load("gdata", "1.s");
        google.setOnLoadCallback(getCalendar);
    });
    function getCalendar() {
    }
})(Zepto, google);
