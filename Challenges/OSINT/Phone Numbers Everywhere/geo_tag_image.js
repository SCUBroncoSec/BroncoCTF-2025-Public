const { ExifTool } = require("exiftool-vendored");

async function geoTagImage(image_path, longitude, latitude) {
  const exif = new ExifTool();
  await exif.write(image_path, {
    GPSLongitude: longitude,
    GPSLatitude: latitude,
  });
  await exif.end();
}


// 37.34914737624593, -121.93858813582675
geoTagImage(
  "/Users/jasonwu/ctf-challenge-maker/images/aws.jpg",
  -121.93858813582675,
  37.34914737624593
)
  .then(() => {
    console.log("task completed");
  })
  .catch((error) => {
    console.error(error);
  });
