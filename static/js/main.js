Dropzone.autoDiscover = false;

const myDropzone = new Dropzone('#my-dropzone', {
  url: 'upload/',
  maxFiles: 20,
  maxFilesize: 2,
  acceptedFiles: '.png, .jpg',
});
