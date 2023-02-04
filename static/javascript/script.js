function toggleForm(btn) {
  var form = btn.nextElementSibling;
  form.classList.toggle("d-none");
}


function toggleStrikethrough(checkbox,param) {
  console.log(param)
  setTimeout(()=>{

  },5000)
  let todoText = checkbox.nextElementSibling;
  if (checkbox.checked) {
    todoText.classList.add("strikethrough");
    window.location.href=(`/updateMark/${param}`)
    console.log(param)
  } else {
    todoText.classList.remove("strikethrough");
    window.location.href=('/RemoveMark/'+param)
    console.log(param)
  }
}
