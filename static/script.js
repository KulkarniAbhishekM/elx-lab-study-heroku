var totalTimer = setInterval(totalCounter, 250);
var quizTimer; // used to see how long quiz is open
var botTimer; // used to see how long bot is open

var db = firebase.database(); // db ref

// counts for time
var countTotal = 0;
var countQuiz = 0;
var countBot = 0;

var openAllowed = false; //chatbot allowed to open after first lesson revealed

// bot interactions
var wantToLearnCount = 0;
var wasThatHelpful = "unanswered";
var botOpenCount = "";
var botCloseCount = "";

// used for db references
var username = "";
var pageID = 0;
var refTotal = "";
var refQuiz = "";
var refBotTime = "";
var refHelpful = "";
var refOpenCount = "";
var refCloseCount = "";
var refLearnCount = "";

var videoStopTime = 0;

function setUp(u, id) {

  username = u;
  pageID = id;
  console.log(username);
  refOpenCount = db.ref(username + "/openCount");
  refCloseCount = db.ref(username + "/closeCount");
  refLearnCount = db.ref(username + "/learnMoreCount");

  if (id == 1) {
    refTotal = db.ref(username + "/experimental/superposition/totalTime");
    refQuiz = db.ref(username + "/experimental/superposition/quizTime");
    refBotTime = db.ref(username + "/experimental/superposition/botTime");
    refHelpful = db.ref(username + "/experimental/superposition/lessonHelpful");
    videoStopTime = 102.0;
  } else if (id == 2) {
    refTotal = db.ref(username + "/experimental/restAPI/totalTime");
    refQuiz = db.ref(username + "/experimental/restAPI/quizTime");
    refBotTime = db.ref(username + "/experimental/restAPI/botTime");
    refHelpful = db.ref(username + "/experimental/restAPI/lessonHelpful");
    videoStopTime = 143.0;
  } else if (id == 3) {
    refTotal = db.ref(username + "/experimental/dns/totalTime");
    refQuiz = db.ref(username + "/experimental/dns/quizTime");
    refBotTime = db.ref(username + "/experimental/dns/botTime");
    refHelpful = db.ref(username + "/experimental/dns/lessonHelpful");
    videoStopTime = 221.0;
  } else if (id == 4){
    refTotal = db.ref(username + "/control/entanglement/totalTime");
    refQuiz = db.ref(username + "/control/entanglement/quizTime");
  } else if (id == 5){
    refTotal = db.ref(username + "/control/cryptography/totalTime");
    refQuiz = db.ref(username + "/control/cryptography/quizTime");
  } else if (id == 6){
    refTotal = db.ref(username + "/control/cloud/totalTime");
    refQuiz = db.ref(username + "/control/cloud/quizTime");
  }

  refLearnCount.on('value', function (snapshot) {
    if (snapshot.val() != null) {
      wantToLearnCount = snapshot.val();
    }
  })

  refOpenCount.on('value', function (snapshot) {
    if (snapshot.val() != null) {
      botOpenCount = snapshot.val();
    }
  })

  refCloseCount.on('value', function (snapshot) {
    if (snapshot.val() != null) {
      botCloseCount = snapshot.val();
    }
  })

}

function addQuizListener(id) {
  var video = document.getElementById("player");

  video.addEventListener('ended', (event) => {

    console.log("the video has ended ");
    document.getElementById("submit-area").style.display = 'block';
    document.getElementById("fake-button").style.display = 'none';
    if (id == 1) {
      document.getElementById("quiz-body").style.display = 'block';
    } else if (id == 2) {
      document.getElementById("quiz-body-2").style.display = 'block';
    } else if (id == 3) {
      document.getElementById("quiz-body-3").style.display = 'block';
    }
    quizTimer = setInterval(quizCounter, 250);

  });
}

function addVideoListener() {
  var video = document.getElementById("player");
  // var stopTime1 = 102.0;

  video.addEventListener('timeupdate', (event) => {

    if (video.currentTime > videoStopTime && video.currentTime < videoStopTime + 0.25) {
      // var bot = document.getElementById("chatbot-text"); //this works
      // bot.style.display = "inline-block";
      openChatbot();
      video.pause();
      openAllowed = true;
    }
  });
}

// shows the lesson
function showLesson() {
  clearInterval(botTimer);
  console.log("set lesson timer");
  botTimer = setInterval(botCounter, 250);


  var moreText = document.getElementById("more-text-A");
  //   var moreText = document.getElementById(item_id);
  moreText.style.display = "inline-block";

  document.getElementById("was-that-helpful").style.display = "inline-block";
  document.getElementById("yes-no-buttons-helpful").style.display = "inline-block";

  wantToLearnCount = wantToLearnCount + 1;
  refLearnCount.set(wantToLearnCount);
  document.getElementById("yes-no-buttons").style.display = 'none';
}

function thanksYes() {
  console.log("thanks");
  document.getElementById("yes-no-buttons-helpful").style.display = 'none';
  document.getElementById("thanks").style.display = 'inline-block';
  refHelpful.set("yes");
}

function thanksNo() {
  console.log("thanks");
  document.getElementById("yes-no-buttons-helpful").style.display = 'none';
  document.getElementById("thanks").style.display = 'inline-block';
  wasThatHelpful = "no";
  refHelpful.set("no");
}

function totalCounter() {
  countTotal = countTotal + 0.25;
}

function quizCounter() {
  countQuiz = countQuiz + 0.25;
}

function botCounter() {
  console.log("bot timer")
  countBot = countBot + 0.25;
}

function openChatbot() {
  if (document.getElementById("chatbot-text").style.display != "inline-block") {
    if (openAllowed) {
      document.getElementById("chatbot-text").style.display = 'inline-block';
      botTimer = setInterval(botCounter, 250);
      refOpenCount.set(++botOpenCount);
      console.log("open bot");
    }
  }

}

function closeChatbot() {
  document.getElementById("chatbot-text").style.display = 'none';
  // botCloseCount = botCloseCount + 1;
  refCloseCount.set(++botCloseCount);
  clearInterval(botTimer);
  console.log("close bot");
}

function updateDatabase() {
  clearInterval(totalTimer);
  clearInterval(quizTimer);

  refTotal.set(countTotal);
  refQuiz.set(countQuiz);
  
  if (pageID == 1 || pageID == 2 || pageID == 3){
    refBotTime.set(countBot);
  }

}
