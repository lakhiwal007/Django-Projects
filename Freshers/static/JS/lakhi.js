let navToggle = "false";

function sideBar() {
  if (navToggle === "false") {
    document.getElementById("sidebar").style.width = '300px';
    document.getElementById("sidebar").style.visibility = "visible";
    document.getElementById("lstIem").style.opacity = "1";
    navToggle = "true";
  } else if (navToggle === "true") {
    document.getElementById("sidebar").style.width = '0px';
    document.getElementById("lstIem").style.opacity = "0";
    navToggle = "false";
  }
}
