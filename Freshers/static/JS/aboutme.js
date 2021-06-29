$(document).ready(function() {
  //About me page
  $(".hide5").click(function() {
    /* Act on the event */
    $("#heading2").hide();
    $("#Iframe-2").hide();
    $("#Iframe-1").show();
    $("#Iframe-3").hide();
  });
  //home page
  $(".hide1").click(function() {
    /* Act on the event */
    $("#heading2").show();
    $("#Iframe-1").hide();
    $("#Iframe-2").hide();
    $("#Iframe-3").hide();
  });
  //Student Corner page
  $(".hide4").click(function() {
    /* Act on the event */
    $("#heading2").hide();
    $("#Iframe-2").show();
    $("#Iframe-1").hide();
    $("#Iframe-3").hide();
  });
  //campusInfo page
  $(".hide3").click(function() {
    /* Act on the event */
    $("#heading2").hide();
    $("#Iframe-3").show();
    $("#Iframe-2").hide();
    $("#Iframe-1").hide();
  });

  $("#SM").click(function(){

    $("#studymaterialToggle").slideToggle('slow');

  });
  $("#CI").click(function(){
    $("#CampusInfo").slideToggle('slow');
  });
  $("#SC").click(function(){
    $("#StdntCrnr").slideToggle('slow');
  });
});
