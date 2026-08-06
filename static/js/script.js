// =============================
// Smooth Scroll Animation
// =============================

document.querySelectorAll('nav a').forEach(anchor => {

    anchor.addEventListener('click', function(e){

        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({

            behavior:'smooth'

        });

    });

});

// =============================
// Navbar Shadow on Scroll
// =============================

window.addEventListener("scroll",function(){

    const nav=document.querySelector("nav");

    if(window.scrollY>50){

        nav.style.boxShadow="0 5px 20px rgba(0,0,0,0.4)";

    }

    else{

        nav.style.boxShadow="none";

    }

});

// =============================
// Hero Text Typing Effect
// =============================

const titles=[

"Python Full Stack Developer",

"BCA Student",

"Aspiring Software Engineer"

];

let index=0;

const heading=document.querySelector(".hero h2");

setInterval(()=>{

heading.innerHTML=titles[index];

index++;

if(index>=titles.length){

index=0;

}

},2000);

// =============================
// Fade Animation
// =============================

const observer=new IntersectionObserver(entries=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.style.opacity="1";

entry.target.style.transform="translateY(0px)";

}

});

});

document.querySelectorAll("section").forEach(section=>{

section.style.opacity="0";

section.style.transform="translateY(50px)";

section.style.transition="1s";

observer.observe(section);

});