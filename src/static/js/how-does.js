const how_does_sec = document.querySelector(".how-does-sec");
const circle_dot = document.querySelectorAll(".circle-dot");
const box = document.querySelectorAll(".how-does-reg");

for (let i = 0; i < circle_dot.length; i++) {
  circle_dot[i].style.opacity = "0";
}
for (let i = 0; i < box.length; i++) {
  box[i].style.opacity = "0.2";
  box[i].style.transform = `translateX(160%)`; // Adjusted the initial translation value
}

if (window.matchMedia("(hover: hover)").matches) {
  // Non-touch device (mouse hover)
  how_does_sec.addEventListener("mouseenter", () => {
    const revealStep = () => {
      let stepIndex = 0;
      const stepInterval = setInterval(() => {
        if (stepIndex % 2 === 0) {
          // Show dot
          let dotIndex = Math.floor(stepIndex / 2);
          let delay_dot = dotIndex * 0.08; // Adjusted the delay duration
          if (dotIndex > 0) {
            delay_dot = dotIndex * 0.08 + 0.1; // Adjusted the delay duration
          }
          circle_dot[dotIndex].style.opacity = "1";
          circle_dot[dotIndex].style.transitionDelay = `${delay_dot}s`;
        } else {
          // Show box item
          let boxIndex = Math.floor(stepIndex / 2);
          let delay_box = boxIndex * 0.1; // Adjusted the delay duration
          if (boxIndex > 0) {
            delay_box = boxIndex * 0.1 + 0.2; // Adjusted the delay duration
          }
          let delay_item = boxIndex * 0.1 + delay_box;
          box[boxIndex].style.opacity = "1";
          box[boxIndex].style.transitionDelay = `${delay_item}s`;
          box[boxIndex].style.transform = "translateX(0)";
          box[boxIndex].style.transitionTimingFunction = "ease"; // Added easing effect
        }

        stepIndex++;

        if (stepIndex >= circle_dot.length + box.length) {
          clearInterval(stepInterval);
        }
      }, 150); // Adjusted the delay duration between steps
    };

    revealStep();
  });
} else {
  // Touch device (tap)
  how_does_sec.addEventListener("touchstart", () => {
    const revealStep = () => {
      let stepIndex = 0;
      const stepInterval = setInterval(() => {
        if (stepIndex % 2 === 0) {
          // Show dot
          let dotIndex = Math.floor(stepIndex / 2);
          let delay_dot = dotIndex * 0.08; // Adjusted the delay duration
          if (dotIndex > 0) {
            delay_dot = dotIndex * 0.08 + 0.1; // Adjusted the delay duration
          }
          circle_dot[dotIndex].style.opacity = "1";
          circle_dot[dotIndex].style.transitionDelay = `${delay_dot}s`;
        } else {
          // Show box item
          let boxIndex = Math.floor(stepIndex / 2);
          let delay_box = boxIndex * 0.1; // Adjusted the delay duration
          if (boxIndex > 0) {
            delay_box = boxIndex * 0.1 + 0.2; // Adjusted the delay duration
          }
          let delay_item = boxIndex * 0.1 + delay_box;
          box[boxIndex].style.opacity = "1";
          box[boxIndex].style.transitionDelay = `${delay_item}s`;
          box[boxIndex].style.transform = "translateX(0)";
          box[boxIndex].style.transitionTimingFunction = "ease"; // Added easing effect
        }

        stepIndex++;

        if (stepIndex >= circle_dot.length + box.length) {
          clearInterval(stepInterval);
        }
      }, 100); // Adjusted the delay duration between steps
    };
    revealStep();
  });
}
