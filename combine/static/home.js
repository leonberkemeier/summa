function myFunction() {
    alert("Hello from a static file!");
  }

// ===== Multitext ======
let typingEffect = new Typed (".multiText",{
    strings:["Coder","Leon","Showman","entertainer"],
    loop: true,
    typeSpeed: 200,
    backSpeed: 300,
    backDelay: 1500,
});
// ====== Modals ===========

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');
const btnsOpenModal = document.querySelectorAll('.show-modal');

const openModal = function () {
    modal.classList.remove('hidden');
    overlay.classList.remove('hidden');
  };

const closeModal = function () {
modal.classList.add('hidden');
overlay.classList.add('hidden');
};

for (let i = 0; i < btnsOpenModal.length; i++)
  btnsOpenModal[i].addEventListener('click', openModal);

btnCloseModal.addEventListener('click', closeModal);
overlay.addEventListener('click', closeModal);


document.addEventListener('keydown', function (e) {
    // console.log(e.key);
  
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeModal();
    }
  });


  // second modal 

  const modal1 = document.querySelector('.modal1');
  const btnCloseModal1 = document.querySelector('.close-modal1');
  const btnsOpenModal1 = document.querySelectorAll('.show-modal1');
  
  const openModal1 = function () {
      modal1.classList.remove('hidden');
      overlay.classList.remove('hidden');
    };
  
  const closeModal1 = function () {
  modal1.classList.add('hidden');
  overlay.classList.add('hidden');
  };
  
  for (let i = 0; i < btnsOpenModal1.length; i++)
    btnsOpenModal1[i].addEventListener('click', openModal1);
  
  btnCloseModal1.addEventListener('click', closeModal1);
  overlay.addEventListener('click', closeModal1);
  
  
  document.addEventListener('keydown', function (e) {
      // console.log(e.key);
    
      if (e.key === 'Escape' && !modal1.classList.contains('hidden')) {
        closeModal1();
      }
    });  

  // third

  const modal2 = document.querySelector('.modal2');
  const btnCloseModal2 = document.querySelector('.close-modal2');
  const btnsOpenModal2 = document.querySelectorAll('.show-modal2');
  
  const openModal2 = function () {
      modal2.classList.remove('hidden');
      overlay.classList.remove('hidden');
    };
  
  const closeModal2 = function () {
  modal2.classList.add('hidden');
  overlay.classList.add('hidden');
  };
  
  for (let i = 0; i < btnsOpenModal2.length; i++)
    btnsOpenModal2[i].addEventListener('click', openModal2);
  
  btnCloseModal2.addEventListener('click', closeModal2);
  overlay.addEventListener('click', closeModal2);
  
  
  document.addEventListener('keydown', function (e) {
      // console.log(e.key);
    
      if (e.key === 'Escape' && !modal2.classList.contains('hidden')) {
        closeModal2();
      }
    });


  // fourth

  const modal3 = document.querySelector('.modal3');
  const btnCloseModal3 = document.querySelector('.close-modal3');
  const btnsOpenModal3 = document.querySelectorAll('.show-modal3');
  
  const openModal3 = function () {
      modal3.classList.remove('hidden');
      overlay.classList.remove('hidden');
    };
  
  const closeModal3 = function () {
  modal3.classList.add('hidden');
  overlay.classList.add('hidden');
  };
  
  for (let i = 0; i < btnsOpenModal3.length; i++)
    btnsOpenModal3[i].addEventListener('click', openModal3);
  
  btnCloseModal3.addEventListener('click', closeModal3);
  overlay.addEventListener('click', closeModal3);
  
  
  document.addEventListener('keydown', function (e) {
      // console.log(e.key);
    
      if (e.key === 'Escape' && !modal3.classList.contains('hidden')) {
        closeModal3();
      }
    });


// ====== Collapsibles =====


var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
};


// ==== Image slider ====

var counter = 1;
    setInterval(function(){
        document.getElementById('radio'+counter).checked=true;
        counter++;
        if(counter>5){
            counter=1;
        }
    }, 5000);


