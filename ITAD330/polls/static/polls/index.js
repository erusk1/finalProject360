// This example adds a marker to indicate the position of Bondi Beach in Sydney,
// Australia.
function initMap() {
  console.log("In JS");
  const data = document.currentScript.dataset;
  const lat1 = parseFloat(data.lat);
  const lon1 = parseFloat(data.lon);
  const latc2 = parseFloat(data.lat1);
  const lonc2 = parseFloat(data.lon1);
  const latc3 = parseFloat(data.lat2);
  const lonc3 = parseFloat(data.lon2);
  const latc4 = parseFloat(data.lat3);
  const lonc4 = parseFloat(data.lon3);
  const latc5 = parseFloat(data.lat4);
  const lonc5 = parseFloat(data.lon4);

  console.log(data.lat);
  console.log(data.lon);
  console.log(data.lat1);
  console.log(data.lon1);
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: { lat: lat1, lng: lon1 },
  });
  const image =
    "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
  const beachMarker = new google.maps.Marker({
    position: { lat: lat1, lng: lon1 },
    map: map,
    title: "Wreck 1"
  });

  const image1 =
    "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
  const beachMarker1 = new google.maps.Marker({
    position: { lat: latc2, lng: lonc2 },
    map: map,
    title: "Wreck 2"
  });

  const image2 =
  "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
const beachMarker2 = new google.maps.Marker({
  position: { lat: latc3, lng: lonc3 },
  map: map,
  title: "Wreck 3"
});

const image3 =
"https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
const beachMarker3 = new google.maps.Marker({
position: { lat: latc4, lng: lonc4 },
map: map,
title: "Wreck 4"
});

const image4 =
"https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
const beachMarker4 = new google.maps.Marker({
position: { lat: latc5, lng: lonc5 },
map: map,
title: "Wreck 5"
});
}

window.initMap = initMap;