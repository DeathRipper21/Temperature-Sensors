# Temperature-Sensors
<h1>Temperature Sensors for Weather Station Development</h1>

<h2>Code is developed to compare the adafruit_mcp9808 temperature sensor and DFROBOT Temperature & Humidity Sensor V2.</h2>
<h2>This code was developed and tested on a Pi Pico</h2>

<table>
  <tr>
    <th>Adafruit_MCP9808</th>
    <th>Connections</th>
  </tr>
  <tr>
    <td>VCC</td>
    <td>GP6</td>
  </tr>
  <tr>
    <td>GND</td>
    <td>GND</td>
  </tr>
  <tr>
    <td>SCL</td>
    <td>GP5</td>
  </tr>
  <tr>
    <td>SDA</td>
    <td>GP4</td>
  </tr>

<h3>Similar principle with the second Adafruit_mcp9808 just add VCC ==> GP7 GND ==> GND SCL ==> GP15 SDA ==> GP14 </h3>

<table>
  <tr>
    <th>DFROBOT Humidity Sensor V2</th>
    <th>Connections</th>
  </tr>
  <tr>
    <td>VCC</td>
    <td>5V</td>
  </tr>
  <tr>
    <td>GND</td>
    <td>GND</td>
  </tr>
  <tr>
    <td>Signal</td>
    <td>GP3</td>
  </tr>
