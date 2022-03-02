document.addEventListener('DOMContentLoaded', () => {

  // Unix timestamp (in seconds) to count down to
  var twoDaysFromNow = Math.floor(new Date('2022.03.10').getTime() / 1000)

  // Set up FlipDown
  var flipdown = new FlipDown(twoDaysFromNow)

    // Start the countdown
    .start()

    // Do something when the countdown ends
    .ifEnded(() => {
      console.log('The countdown has ended!');
    });

  var ver = document.getElementById('ver');
  ver.innerHTML = flipdown.version;
});