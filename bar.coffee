command: "curl --silent http://127.0.0.1:5000/"

# the refresh frequency in milliseconds
refreshFrequency: 1000

render: (_) -> """
<table>
  <tr>
    <td class=align-left><div class='time'></div></td>
    <td class=align-middle><div class='track'></div></td>
    <td class=align-right><div class='battery'></div></td>
  <tr>
</table>
"""

update: (output, domEl) ->
  parsed = JSON.parse(output)
  #$(domEl).find('.track').text(parsed.playing)
  $(domEl).find('.time').text(parsed.time)
  if Object.keys(parsed.track).length is 0
    track = ''
  else
    track = parsed.track.name + ' - ' + parsed.track.album + ' - ' + parsed.track.artist
  $(domEl).find('.track').text(track)
  $(domEl).find('.battery').text(parsed.battery.percent)


style: """
  background: rgba(#1d2021, 0.99)

  -webkit-backdrop-filter: blur(20px)
  border-radius: 2px
  border: 2px solid #1d2021
  box-sizing: border-box
  color: #fff

  font-family: Iosevka
  font-size: 12px

  left: 20px
  right: 20px
  bottom: 10px
  height: 20px
  
  padding: 0px 0px 10px 10px

  align-middle
    text-align: center
    vertical-align: middle

  align-left
    text-align: left

  align-right
    text-align: right

  p
    margin: 0px 0px 0px

  table
    margin-top: -2px
    width: 100%
"""
