function change_name(input) {
    let file = input.files[0];
    document.getElementById('button-text').innerHTML = file.name
    let fr = new FileReader();
    fr.onload = function () {
        document.getElementById('question-image').src = fr.result;
    }
    fr.readAsDataURL(file)
}
