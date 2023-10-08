const dropArea = document.getElementById("drop-area");
const fileElem = document.getElementById("fileElem");
const uploadButton = document.getElementById("upload-button");

// Prevent default drag behaviors
["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
  dropArea.addEventListener(eventName, preventDefaults, false);
});

// Highlight drop area when a file is dragged over it
dropArea.addEventListener("dragenter", highlight, false);
dropArea.addEventListener("dragover", highlight, false);
dropArea.addEventListener("dragleave", unhighlight, false);
dropArea.addEventListener("drop", unhighlight, false);

// Handle dropped files
dropArea.addEventListener("drop", handleDrop, false);

// Handle file input change
fileElem.addEventListener("change", handleFilesFromInput, false);

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

function highlight() {
  dropArea.classList.add("highlight");
}

function unhighlight() {
  dropArea.classList.remove("highlight");
}

function handleDrop(e) {
  e.preventDefault();
  const dt = e.dataTransfer;
  const files = dt.files;

  // Append the dropped files to the file input
  fileElem.files = files;

  // Handle the dropped files
  handleFiles(files);
}

function handleFilesFromInput() {
  const files = fileElem.files;
  handleFiles(files);
}

function handleFiles(files) {
  files = [...files];
  files.forEach(uploadFile);
}

function uploadFile(file) {
  const url = "/upload";
  const formData = new FormData();

  formData.append("file", file);

  fetch(url, {
    method: "POST",
    body: formData,
  })
    .then((response) => response.text())
    .then((data) => {
      console.log(data);
    });
}
const mypdf=document.querySelector('#mypdf');
const upload_popup=document.querySelector('.upload-popup');
const btn_close=document.querySelector('.close-btn');
const overlay=document.querySelector('.overlay');
const body=document.querySelector('.bod');
mypdf.addEventListener("click", function () {
    upload_popup.classList.remove("hidden");
    overlay.classList.remove("hidden");
    body.classList.add('overflow-hid');
  });
btn_close.addEventListener("click", function () {
    upload_popup.classList.add("hidden");
    overlay.classList.add("hidden");
    body.classList.remove('overflow-hid');
  });
overlay.addEventListener("click", function () {
    upload_popup.classList.add("hidden");
    overlay.classList.add("hidden");
    body.classList.remove('overflow-hid');
  });

/*
function uploadForm() {
  // Trigger the form submission when the upload button is clicked
  document.querySelector(".my-form").submit();
}
function handleFileSelect(event) {
var file = event.target.files[0];
var formData = new FormData();
formData.append('file', file);

// Create a new XMLHttpRequest object
var xhr = new XMLHttpRequest();

// Set up request
xhr.open('POST', '/upload', true);

// Set up callback function for when the request completes
xhr.onload = function() {
  if (xhr.status === 200) {
    // File uploaded successfully
    console.log('File uploaded.');
  } else {
    // An error occurred while uploading the file
    console.log('An error occurred while uploading the file.');
  }
};

// Send the request with the form data
xhr.send(formData);*/