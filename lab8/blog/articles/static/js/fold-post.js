var foldBtns = document.getElementsByClassName("fold-button");
document.addEventListener("DOMContentLoaded", function () {
  let foldBtns = document.querySelectorAll(".fold-button");

  foldBtns.forEach(function (button) {
    button.addEventListener("click", function () {
      // Находим родительский элемент статьи
      let articlePreview = this.closest(".one-post");

      // Переключаем класс folded у родительского элемента
      articlePreview.classList.toggle("folded");

      // Меняем текст кнопки в зависимости от наличия класса folded
      if (articlePreview.classList.contains("folded")) {
        this.textContent = "Развернуть";
      } else {
        this.textContent = "Свернуть";
      }
    });
  });
});
