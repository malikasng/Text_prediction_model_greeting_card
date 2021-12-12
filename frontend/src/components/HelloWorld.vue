<template>


  <div class="centered-container">
    <md-content class="md-query" id="page" style="margin: 75px;">

      <!-- START OF QUERY -->

      <div v-if="onceAppear" class="icon-bar" align="left" style="visibility: visible; height: auto; margin: 15px" >
          <button class="backgroundButton" @click="lighterBackground()"><emoji name="sunny" size="15"/></button>
          <button class="backgroundButton" @click="darkerBackground()"><emoji name="crescent_moon" size="15"/></button>
          <button class="backgroundButton" @click="xmasSpiritBackground()"><emoji name="christmas_tree" size="15"/></button>
      </div>

      <!-- QUERY TIMEOUT-->

      <!-- START OF ALWAYS SHOW-->


      <div class="alwaysShow" id="alwaysShow" style="margin: 15px">
        <div style="text-align: center;">
        <img src="../assets/LogoWithoutBackground.png"/>
        <p style="font-size: xx-small">Copyright ©2021 by G2-20. All rights reserved.</p>
          <br>
        </div>
      </div>

      <!--END OF ALWAYSSHOW-->

      <!--QUERY CONTINUES -->

      <div class="query" id="query" v-if="queryAppear" style="margin: 15px">
          <div>
            <p style="font-size: large">Welcome to New Year's Card Generator 2000 <emoji name="tm" size="20"/></p>

            <md-field class="question" id="recipient">
              <label class="answerPlaceholder" id="Placeholder">Recipient's Name</label>
              <md-input class="mandatoryEntry" id="mandatoryEntryRecipient" v-model="nameRecipient" required maxlength="30"></md-input>
            </md-field>

            <md-field class="question" id="sender">
              <label class="answerPlaceholder">Sender's Name </label>
              <md-input class="mandatoryEntry" id="mandatoryEntrySender" v-model="nameSender" required maxlength="30"></md-input>
            </md-field>

            <md-field class="question" id="relationship">
              <label class="answerPlaceholder">(Optional) Relationship Status </label>
              <md-select class="mandatoryEntry" v-model="relationship" name="relationship" id="relationship">
                <md-option class="option" value="family" >Family</md-option>
                <md-option class="option" value="friend">Friend</md-option>
                <md-option class="option" value="romantic">Romantic</md-option>
                <md-option class="option" value="colleague">Colleague</md-option>
              </md-select>
              <md-dialog-alert
                  :md-active.sync="infoButton"
                  :md-content="infoButtonMessage"
                  md-confirm-text="Cool!" />
          <md-button style="background-color: darkred;border-radius: 30%" @click="infoButton = true"><p class="dialogButtonText">?</p>
          </md-button>
            </md-field>
          </div>

          <br>
          <div class="question" id="literacy">
            <div>Literacy Type:</div>
            <md-radio v-model="literacy" value="prosa">Prosa</md-radio>
            <md-radio v-model="literacy" value="prosa_sentence">Prosa (Sentenced-Based/Experimental)</md-radio>
            <md-radio v-model="literacy" value="poem">Poem</md-radio>
            <md-radio v-model="literacy" value="haiku">Haiku</md-radio>
          </div>

          <br>
          <div>
            <div>Degree of Formality:</div>
            <div style="margin-right: 20%; margin-left: 20%">
              <vue-slider
                ref="slider"
                v-model="value"
                v-bind="options"
              >
              </vue-slider>
            </div>

            <br>
          </div>

          <div>
            <button class="christmasButton" @click="submit()" >New Year's Card</button>
          </div>

          <md-snackbar :md-position=center :md-duration="isInfinity ? Infinity : duration" :md-active.sync="showSnackbar" md-persistent>
            <span>Connection timeout. Showing limited messages!</span>
            <md-button class="md-primary" @click="showSnackbar = false">Retry</md-button>
          </md-snackbar>

        <br><br>

          <div class="chinese" id="chinese">
            <div>
              <emoji name="rat" size="100"/>
              <p style="font-family: Harakiri,serif; font-size: medium"> 2020</p>
            </div>

            <div style="font-size: x-large" >
              <p>For A Limited Time: CHINESE NEW YEAR  </p>
              <br>
              <div style="font-family: Harakiri,serif">
                <Countdown end="February 12, 2021" showDays showHours showMinutes showSeconds></Countdown>
              </div>
              <br>
              <button class="chineseButton" @click="chineseSubmit()">
                <p class="chineseButtonWriting">CHINESE NEW YEAR'S CARD</p>
              </button>
            </div>

            <div>
              <emoji name="ox" size="100"/>
              <p style="font-family: Harakiri,serif; font-size: medium">2021</p></div>
          </div>

          <br>

          <div class="restBackground">
            <md-toolbar :md-elevation="2" class="restBackground">
              <h1>Coming Soon!!</h1>
            </md-toolbar>

            <md-list class="restBackground">
              <md-subheader class="restTag">New Language Options</md-subheader>
              <md-list-item>
                <div style="margin: auto;">
                  <p class="rest"><country-flag country='de' size='normal' style="vertical-align: text-top"/>  Deutsch </p>
                  <p class="rest"><country-flag country='fr' size='normal' style="vertical-align: text-top"/>  Français</p>
                </div>
                <div style="margin: auto;">
                  <p class="rest"><country-flag country='tr' size='normal' style="vertical-align: text-top"/>  Türkçe</p>
                  <p class="rest"><country-flag country='gr' size='normal' style="vertical-align: text-top"/>  Ελληνικά</p>
                </div>
                <div style="margin: auto">
                  <p class="rest"><country-flag country='cn' size='normal' style="vertical-align: text-top"/>  普通話</p>
                  <p class="rest"><country-flag country='ua' size='normal' style="vertical-align: text-top"/>  Український</p>
                </div>
              </md-list-item>

              <md-divider></md-divider>

              <md-subheader class="restTag">Moods</md-subheader>
              <md-list-item>
                <div style="margin: auto">
                  <p class="rest"><emoji name="flushed" size="20"/>  Emotional / Sincere</p>
                  <p class="rest"><emoji name="joy" size="20"/>  Funny with Jokes </p>
                  <p class="rest"><emoji name="smile" size="20"/>  Happy </p>
                  <p class="rest"><emoji name="100" size="20"/>  Highly Optimist </p>
                </div>
                <div style="margin: auto">
                  <p class="rest"><emoji name="angel" size="20"/>  Innocent </p>
                  <p class="rest"><emoji name="clipboard" size="20"/>  Professional </p>
                  <p class="rest"><emoji name="pray" size="20"/>  Spiritual </p>
                </div>
              </md-list-item>

              <md-divider style="border-top: 1px solid revert"></md-divider>

              <md-subheader class="restTag">Expectations</md-subheader>
              <md-list-item>
                <div style="margin: auto">
                  <p class="rest"><emoji name="briefcase" size="20"/>  Career / Promotion </p>
                  <p class="rest"><emoji name="clinking_glasses" size="20"/>  Entertainment </p>
                </div>
                <div style="margin: auto">
                  <p class="rest"><emoji name="syringe" size="20"/>  Health </p>
                  <p class="rest"><emoji name="moneybag" size="20"/>  Money</p>
                </div>
                <div style="margin: auto">
                  <p class="rest"><emoji name="cupid" size="20"/>  Love </p>
                  <p class="rest"><emoji name="airplane" size="20"/>  Travel </p>
                </div>
              </md-list-item>

              <md-divider></md-divider>

              <md-subheader class="restTag">Advanced Background Application</md-subheader>
              <md-list-item>

                <md-dialog-alert
                    :md-active.sync="ownBackgroundButton"
                    :md-content="ownBackgroundButtonMessage"
                    md-confirm-text="Cool!" />
                <md-button class="dialogButton" @click="ownBackgroundButton = true"><p class="dialogButtonText">INFO: Own Background</p></md-button>

                <md-dialog-alert
                  :md-active.sync="themeGeneratorButton"
                  :md-content="themeGeneratorButtonMessage"
                  md-confirm-text="Cool!" />
                <md-button class="dialogButton" @click="themeGeneratorButton = true"><p class="dialogButtonText">INFO: Background Through Theme Generator</p></md-button>

                <md-dialog-alert
                    :md-active.sync="ganBackgroundButton"
                    :md-content="ganBackgroundButtonMessage"
                    md-confirm-text="Cool!" />
                <md-button class="dialogButton" @click="ganBackgroundButton = true"><p class="dialogButtonText">INFO: GanBackground</p></md-button>
              </md-list-item>
            </md-list>
          </div>

          <footer>
            This website was generated by G2-20 for Komputer und Creativität. For further information:
            <a href="https://www.ei.tum.de/ldv/lehre/komputer-u-creativitaet/">
              Click Here
            </a>
          </footer>
      </div>

      <!--END OF QUERY -->




      <!--START OF LOADING SECTION -->

      <div class="showAfterSubmit" v-if="loadingAppear" style="margin: 15px">
      <p class="showAfterSubmitText" style="font-size: larger"> Please wait...Your submission is being processed, generated cards will be ready shortly! </p>
          <md-progress-spinner class="md-accent showAfterSubmit" md-mode="indeterminate"></md-progress-spinner>
        <div>
          <progress value="0" :max="timeToLoad" id="progressBar"></progress>
        </div>
        <button class="christmasButton" style="visibility: hidden" id="showButton" @click="openShowcase()" >Show Generated Cards</button>
      </div>

      <!--END OF LOADING SECTION -->

      <!--START OF SHOWCASE SECTION -->


      <div class="showcase" id="showcase" v-if="showcaseAppear" style="margin: 15px">

        <p style="font-size: 40pt; font-family: 'Christmas Flakes',serif;">G2-20 New Year's Cards</p>
        <div id="gallery-wrap1" class="gallery-wrap deck" v-if="backgroundSet===1">
          <div id="pictureCell1" class="">
            <div id="item1" class="item deckCell cardBackground1" @click="chooseCard(1)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{firstText}}</p>
            </div>
          </div>
          <div id="pictureCell2" class="">
            <div id="item2" class="item deckCell cardBackground2" @click="chooseCard(2)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{secondText}}</p>
            </div>
          </div>
          <div id="pictureCell3" class="">
            <div id="item3" class="item deckCell cardBackground3" @click="chooseCard(3)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{thirdText}}</p>
            </div>
          </div>
        </div>
        <div id="gallery-wrap2" class="gallery-wrap deck" v-if="backgroundSet===2">
          <div id="pictureCell4" class="">
            <div id="item4" class="item deckCell cardBackground4" @click="chooseCard(4)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{firstText}}</p>
            </div>
          </div>
          <div id="pictureCell5" class="">
            <div id="item5" class="item deckCell cardBackground5" @click="chooseCard(5)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{secondText}}</p>
            </div>
          </div>
          <div id="pictureCell6" class="">
            <div id="item6" class="item deckCell cardBackground6" @click="chooseCard(6)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{thirdText}}</p>
            </div>
          </div>
        </div>
        <div id="gallery-wrap3" class="gallery-wrap deck" v-if="backgroundSet===3">
          <div id="pictureCell7" class="">
            <div id="item7" class="item deckCell cardBackground7" @click="chooseCard(7)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{firstText}}</p>
            </div>
          </div>
          <div id="pictureCell8" class="">
            <div id="item8" class="item deckCell cardBackground8" @click="chooseCard(8)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{secondText}}</p>
            </div>
          </div>
          <div id="pictureCell9" class="">
            <div id="item9" class="item deckCell cardBackground9" @click="chooseCard(9)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{thirdText}}</p>
            </div>
          </div>
        </div>
        <div id="gallery-wrap4" class="gallery-wrap deck" v-if="backgroundSet===4">
          <div id="pictureCell10" class="">
            <div id="item10" class="item deckCell cardBackground10" @click="chooseCard(10)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{firstText}}</p>
            </div>
          </div>
          <div id="pictureCell11" class="">
            <div id="item11" class="item deckCell cardBackground11" @click="chooseCard(11)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{secondText}}</p>
            </div>
          </div>
          <div id="pictureCell12" class="">
            <div id="item12" class="item deckCell cardBackground12" @click="chooseCard(12)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{thirdText}}</p>
            </div>
          </div>
        </div>
        <div id="gallery-wrap5" class="gallery-wrap deck" v-if="backgroundSet===5">
          <div id="pictureCell13" class="">
            <div id="item13" class="item deckCell cardBackground13" @click="chooseCard(13)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{firstText}}</p>
            </div>
          </div>
          <div id="pictureCell14" class="">
            <div id="item14" class="item deckCell cardBackground14" @click="chooseCard(14)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{secondText}}</p>
            </div>
          </div>
          <div id="pictureCell15" class="">
            <div  id="item15" class="item deckCell cardBackground15" @click="chooseCard(15)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{thirdText}}</p>
            </div>
          </div>
        </div>
        <div id="gallery-wrap6" class="gallery-wrap deck" v-if="backgroundSet===6">
          <div id="pictureCell16" class="">
            <div  id="item116" class="item deckCell cardBackground16" @click="chooseCard(16)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{firstText}}</p>
            </div>
          </div>
          <div id="pictureCell17" class="">
            <div  id="item17" class="item deckCell cardBackground17" @click="chooseCard(17)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{secondText}}</p>
            </div>
          </div>
          <div id="pictureCell18" class="">
            <div id="item18" class="item deckCell cardBackground18" @click="chooseCard(18)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{thirdText}}</p>
            </div>
          </div>
        </div>
        <div id="gallery-wrap7" class="gallery-wrap deck" v-if="backgroundSet===7">
          <div id="pictureCell19" class="">
            <div id="item19" class="item deckCell cardBackground19" @click="chooseCard(19)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{firstText}}</p>
            </div>
          </div>
          <div id="pictureCell20" class="">
            <div  id="item20" class="item deckCell cardBackground20" @click="chooseCard(20)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{secondText}}</p>
            </div>
          </div>
          <div id="pictureCell21" class="">
            <div id="item21" class="item deckCell cardBackground21" @click="chooseCard(21)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{thirdText}}</p>
            </div>
          </div>
        </div>
        <div id="gallery-wrap8" class="gallery-wrap deck" v-if="backgroundSet===8">
          <div id="pictureCell22" class="">
            <div id="item22" class="item deckCell cardBackground22" @click="chooseCard(22)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{firstText}}</p>
            </div>
          </div>
          <div id="pictureCell23" class="">
            <div id="item23" class="item deckCell cardBackground23" @click="chooseCard(23)">
              <p  class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{secondText}}</p>
            </div>
          </div>
          <div id="pictureCell24" class="">
            <div id="item24" class="item deckCell cardBackground24" @click="chooseCard(24)">
              <p class="textOnCard" style="text-align: center; margin: 4px; padding: 70px 0"> {{thirdText}}</p>
            </div>
          </div>
          </div>
        </div>


        <br> <br>
         <div class="showcaseButtons" id="showcaseButtons" v-if="showcaseAppear">
         <button style="margin: auto" class="christmasButton" @click="print()">Confirm Card Selection</button>
           <br><br>
           <div>
             <md-button style="background-color: #8b0000;margin: fill" @click="getOtherCards()" >
          <p class="dialogButtonText" style="text-align: right"> Get Other Cards </p>
        </md-button>
             <md-button style="background-color: darkred; margin: fill" @click="openAddSentence()">
          <p class="dialogButtonText" style="text-align: right "> Add Sentence To Algorithm</p>
        </md-button>
             <md-button style="background-color: darkred;margin: fill" @click="openQuery()">
          <p class="dialogButtonText" style="text-align: right" > Return To Query</p>
        </md-button>
        </div>
           </div>
      <!-- END OF DEFAULT SHOWCASE-->

      <!-- START OF SHOWCASE ADD-ON1 -->

      <div v-if="addSentenceAppear">
            <md-field class="question" id="addSentence">
              <label class="answerPlaceholder" id="sentencePlaceholder">Type Sentence You Would Like To Add</label>
              <md-input class="mandatoryEntry" id="addedSentence" v-model="newLine" required maxlength="250" >
              </md-input>
            </md-field>

            <md-button style="background-color: darkred;margin: fill" @click="sendFeedback()">
                 <p class="dialogButtonText" style="text-align: right" > Add My Sentence</p>
                 </md-button>
      </div>
      <!-- END OF SHOWCASE ADD-ON1 -->
      <!-- START OF SHOWCASE ADD-ON2 -->
      <div v-if="processedAppear">
        <p> Your sentence proposal is saved and will be taken into consideration...</p>
      </div>
      <!-- END OF SHOWCASE ADD-ON2 -->
    </md-content>
  </div>


  </template>





<script>
import Emoji from 'vuejs-emojis'
import Countdown from 'countdown-vue'
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'
import { getAPI } from "@/axios";



export default {
  name: 'HelloWorld',
  components: {Emoji, Countdown,VueSlider},
  data: () => ({
    generatedText: ['','',''],
    showResults: false,
    nameRecipient: '',
    nameSender: '',
    relationship: 'friends',
    literacy: 'prosa',
    value: 0,
    duration: 4000,
    name: null,
    algorithm: 'word-based',
    formality: '',
    background: null,
    themeGeneratorButton: false,
    ganBackgroundButton: false,
    ownBackgroundButton: false,
    infoButton: false,
    themeGeneratorButtonMessage: "This function will only be applied to prosa literacy type. It searches for a descriptive word used and forms a card theme accordingly. Chosen theme will be used by AI-Algorithm to select an appropriate theme." +
        "Example: If the word kids and snow are mentioned in the text background may contain kids playing snowball.",
    ganBackgroundButtonMessage: "This function asks for a word from the client, then does a research on web database. AI chooses appropriate pictures, which will be combined to create a brand new picture. This fully by AI-Generated picture will be used as the background.",
    infoButtonMessage: "This function is optional. When no entry is made the default relationship status is set to friends",
    ownBackgroundButtonMessage: "This function asks for a user selected picture, resizes it to 17:22 and uses as the background.",
    queryAppear: true,
    onceAppear: true,
    loadingAppear: false,
    showcaseAppear: false,
    timeToLoad: 5,
    cardNewChosen: 0,
    cardAlreadyChosen: 0,
    addSentenceAppear: false,
    processedAppear: false,
    newLine: '',
    feedback: '',
    chineseTheme: false,
    backgroundSet: 0,
    firstText: '',
    secondText: '',
    thirdText: '',
    selectedTheme: 'light',
  }),
  props: {
    msg: String
  },
  methods: {
    lighterBackground() {
      this.selectedTheme = 'light';
      document.getElementById("query").style.backgroundColor = "white"
      document.getElementById("query").style.color = "black"
      document.getElementById("alwaysShow").style.backgroundColor = "white";
      document.getElementById("alwaysShow").style.color = "black";
      document.getElementById("page").style.backgroundColor = "white"
      document.getElementById("page").style.color = "black"

      let questions = document.getElementsByClassName("question");
      for (let i = 0; i < questions.length; i++) {
        questions[i].style.backgroundColor = 'white';
      }
      let placeholders = document.getElementsByClassName("answerPlaceholder");
      for (let i = 0; i < placeholders.length; i++) {
        placeholders[i].style.color = 'gray';
      }
      let restBackground = document.getElementsByClassName("restBackground");
      for (let i = 0; i < restBackground.length; i++) {
        restBackground[i].style.background = 'white';

      }

      let rest = document.getElementsByClassName("rest");
      for (let i = 0; i < rest.length; i++) {
        rest[i].style.color = 'black';
      }
      let restTag = document.getElementsByClassName("restTag");
      for (let i = 0; i < restTag.length; i++) {
        restTag[i].style.color = 'gray';
      }
      document.getElementById("showAfterSubmit").style.backgroundColor = 'white';
      document.getElementById("showAfterSubmit").style.color = 'black';
      document.getElementById("showAfterSubmitText").style.backgroundColor = 'white';
      document.getElementById("showAfterSubmitText").style.color = 'black';
      document.getElementById("showcaseButtons").style.backgroundColor = 'white';
    },

    darkerBackground() {
      this.selectedTheme = 'dark'
      document.getElementById("query").style.backgroundColor = "gray"
      document.getElementById("query").style.color = "white"
      document.getElementById("alwaysShow").style.backgroundColor = "gray";
      document.getElementById("alwaysShow").style.color = "white";
      document.getElementById("page").style.backgroundColor = "gray"
      document.getElementById("page").style.color = "white"

      let questions = document.getElementsByClassName("question");
      for (let i = 0; i < questions.length; i++) {
        questions[i].style.backgroundColor = 'gray';
      }
      let placeholders = document.getElementsByClassName("answerPlaceholder");
      for (let i = 0; i < placeholders.length; i++) {
        placeholders[i].style.color = 'white';
      }
      let restBackground = document.getElementsByClassName("restBackground");
      for (let i = 0; i < restBackground.length; i++) {
        restBackground[i].style.background = 'gray';
      }

      let rest = document.getElementsByClassName("rest");
      for (let i = 0; i < rest.length; i++) {
        rest[i].style.color = 'white';
      }
      let restTag = document.getElementsByClassName("restTag");
      for (let i = 0; i < restTag.length; i++) {
        restTag[i].style.color = 'white';
      }
      document.getElementById("showAfterSubmit").style.backgroundColor = 'gray';
      document.getElementById("showAfterSubmit").style.color = 'white';
      document.getElementById("showAfterSubmitText").style.backgroundColor = 'gray';
      document.getElementById("showAfterSubmitText").style.color = 'white';
      document.getElementById("showcaseButtons").style.backgroundColor = 'gray';
    },


    xmasSpiritBackground() {
      this.selectedTheme ='xmas'
      document.getElementById("page").style.backgroundColor = "green";
      document.getElementById("page").style.color = "red";
      document.getElementById("alwaysShow").style.backgroundColor = "green";
      document.getElementById("alwaysShow").style.color = "red";
      document.getElementById("query").style.backgroundColor = "green"
      document.getElementById("query").style.color = "red"
      let questions = document.getElementsByClassName("question");
      for (let i = 0; i < questions.length; i++) {
        questions[i].style.backgroundColor = 'green';
      }

      let placeholders = document.getElementsByClassName("answerPlaceholder");
      for (let i = 0; i < placeholders.length; i++) {
        placeholders[i].style.color = 'red';
      }

      let restBackground = document.getElementsByClassName("restBackground");
      for (let i = 0; i < restBackground.length; i++) {
        restBackground[i].style.background = 'green';
      }

      let rest = document.getElementsByClassName("rest");
      for (let i = 0; i < rest.length; i++) {
        rest[i].style.color = 'red';
      }

      let restTag = document.getElementsByClassName("restTag");
      for (let i = 0; i < restTag.length; i++) {
        restTag[i].style.color = 'red';
      }
      document.getElementById("showAfterSubmit").style.backgroundColor = 'green';
      document.getElementById("showAfterSubmit").style.color = 'red';
      document.getElementById("showAfterSubmitText").style.backgroundColor = 'green';
      document.getElementById("showAfterSubmitText").style.color = 'red';
      document.getElementById("showcaseButtons").style.backgroundColor = 'green';
    },


    submit() {
      if (this.relationship==='')
      {
        this.relationship = 'friend';
      }
      if (this.value >= 50){
        this.formality = 'formal'
      }
      else{
        this.formality = 'informal'
      }
      if ((document.getElementById("mandatoryEntryRecipient").value.length !== 0) && (document.getElementById("mandatoryEntrySender").value.length !== 0)) {
        this.openLoading();
        this.sendInformation();
      }
      else {
        alert("Submission failed due to missing information. Please make sure all mandatory fields are filled.")
      }
    },

    chineseSubmit(){
      this.chineseTheme = true;
      this.submit()
    },

    sendFeedback(){
      this.processedAppear = true;
      this.addSentenceAppear = false;
      this.feedback ="feedback";
      this.sendInformation();
    },


    sendInformation(){
      getAPI
      .post("/predict", {
          input_name: this.nameRecipient,
          input_relationship: this.relationship,
          input_textform: this.literacy,
          input_newLine: this.newLine,
          input_feedback: this.feedback,
      })
      .then(response => {
        console.log("received data successfully");
        this.generatedText = response.data;
        console.log(response.data)
      })
      .catch(err => {
        console.log(err);
        console.log(err.data);
        console.log(err.status);
      });
      },

    openShowcase() {
      this.shuffleGeneratedSentences();
      this.loadingAppear = false;
      this.showcaseAppear = true;

    },

    openQuery(){
      location.reload();
    },

    chooseCard(number){
      console.log("chooseCardTriggered");
      if(this.cardAlreadyChosen !==0){
        let cardAlreadyChosenCellName = '';
        cardAlreadyChosenCellName = "pictureCell"+this.cardAlreadyChosen.toString();
        document.getElementById(cardAlreadyChosenCellName).className = '';
      }
      this.cardNewChosen = number;
      this.cardAlreadyChosen = this.cardNewChosen;
      console.log("chooseCard classes emptied");

      let cardNewChosenCellName = '';
        cardNewChosenCellName = "pictureCell"+this.cardNewChosen.toString();
        document.getElementById(cardNewChosenCellName).className += 'active';
    },

    shuffleGeneratedSentences(){
      let firstAssign = 0,secondAssign = 0,thirdAssign = 0;
      while (firstAssign === secondAssign){
        firstAssign = this.getRandomIntInclusive(1,3)
        secondAssign = this.getRandomIntInclusive(1,3)
      }
      thirdAssign = 6 - firstAssign -secondAssign;
      this.firstText = this.generatedText[firstAssign-1];
      this.firstText = this.firstText + "\n" + this.nameSender;
      this.secondText = this.generatedText[secondAssign-1];
      this.secondText = this.secondText + "\n" + this.nameSender;
      this.thirdText = this.generatedText[thirdAssign-1];
      this.thirdText = this.thirdText + "\n" + this.nameSender;
    },

    openAddSentence(){
      this.addSentenceAppear=true;
    },

    print(){
      if(this.cardAlreadyChosen !==0) {
        let chosenItemName, chosenItem;
        chosenItemName = "pictureCell" + this.cardAlreadyChosen.toString();
        chosenItem = document.getElementById(chosenItemName);
        const prtHtml = chosenItem.innerHTML;
        let stylesHtml = '';
        for (const node of [...document.querySelectorAll('link[rel="stylesheet"], style')]) {
          stylesHtml += node.outerHTML;
        }
        const WinPrint = window.open('', '', 'left=0,top=0,width=800,height=900,toolbar=0,scrollbars=0,status=0');
        WinPrint.document.write(`<!DOCTYPE html>
        <html>
          <head>
           ${stylesHtml}
          </head>
          <body>
            ${prtHtml}
          </body>
        </html>`);
        WinPrint.document.close();
        WinPrint.focus();
        //WPrint.print();
      }
      else{
        alert("Please choose a card!")
      }
    },

    openLoading(){
      this.loadingAppear=true;
      this.onceAppear = false;
      this.queryAppear =false;
      this.addSentenceAppear =false;
      this.showcaseAppear = false;
      this.setCardBackgroundNumbers();
      let timeToLoad = this.timeToLoad;
        let timeLeft = timeToLoad;
        const downloadTimer = setInterval(function () {
          if (timeLeft <= 0) {
            clearInterval(downloadTimer);
          }
          document.getElementById("progressBar").value = timeToLoad - timeLeft;
          timeLeft -= 1;
        }, 1000);
        let timeout = 1000*timeToLoad +1000;
        setTimeout(function() {
          document.getElementById("showButton").style.visibility= "visible";
        }, timeout);
    },

    getOtherCards(){
      this.feedback="";
      this.openLoading();
      this.sendInformation();
    },

    getRandomIntInclusive(min, max) {
      min = Math.ceil(min);
      max = Math.floor(max);
      return Math.floor(Math.random() * (max - min + 1) + min); //The maximum is inclusive and the minimum is inclusive
    },

    setCardBackgroundNumbers(){
      if(this.chineseTheme===false){
          this.backgroundSet = this.getRandomIntInclusive(1,6);
        }
      else {
          this.backgroundSet = this.getRandomIntInclusive(7,8);
        }
    },
  },


}

</script>





<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .centered-container {
    min-height: 100vh;
    display: flex;
    text-align: center;
    align-items: center;
    justify-content: center;
    position: relative;
    background: linear-gradient(to left, #09ea9e,#4ab7aa,#46a19e,#58939f,#777ba3,#876fa5,#8d6aa6,#be62bc);
    }

  img {
    min-width: 80px;
  }

  .icon-bar {
    width: 107px;
  }

  .backgroundButton{
    border-radius: 100%;
    background-color: lightgray;
  }

  .query{
    background-color: white;
    color: black;
  }

  .chinese{
    align-items: center;
    display: flex;
    justify-content: center;
    background-image: url("../assets/chinese-new-year-lanterns.jpg");
    background-size: cover;
    height: 400px;
    color: yellow;
    font-family: "Chinese TakeAway",serif;
  }
  .chineseButton {
    background-color: transparent;
    display: inline-block;
    -webkit-box-sizing:border-box;
       -moz-box-sizing:border-box;
            box-sizing:border-box;
    min-width:100px;
    padding: 22px 33px;
    color: #FFF;
    text-shadow: 0 1px 2px rgba(0,0,0,0.75);
    outline: none;
    border-radius: 15px;
    border: 1px solid #4c0300;
    box-shadow:
      inset 1px 1px 0px rgba(255,255,255,0.25), /* highlight */
      inset 0 0 6px #a23227, /* inner glow */
      inset 0 80px 80px -40px #ac3223, /* gradient */
      1px 1px 3px rgba(0,0,0,0.75); /* shadow */

    position: relative;
    overflow: visible; /* IE9 & 10 */
    -webkit-transition: 500ms linear;
       -moz-transition: 500ms linear;
         -o-transition: 500ms linear;
            transition: 500ms linear;
}

.chineseButton::before {
  content: '';
  display: block;
  position: absolute;
  top: -7px;
  left: -3px;
  right: 0;
  height: 23px;
}
.chineseButton:hover {
  background: #a61715;
  text-shadow: 0 1px 2px rgba(0,0,0,0.75), 0 0 40px #FFF;
  box-shadow:
    inset 1px 1px 0px rgba(255,255,255,0.25), /* highlight */
    inset 0 0 6px #da3b2c, /* inner glow */
    inset 0 80px 80px -40px #dd4330, /* gradient */
    1px 1px 3px rgba(0,0,0,0.75); /* shadow */

}
.chineseButton:focus {
  outline: none; /*FF*/
}
.chineseButton:active {
  box-shadow:
    inset 1px 1px 0px rgba(255,255,255,0.25), /* highlight */
    inset 0 0 6px #da3b2c, /* inner glow */
    inset 0 80px 80px -40px #dd4330, /* gradient */
    0px 1px 0px rgba(255,255,255,0.25); /* shadow */

  -webkit-transition: 50ms linear;
     -moz-transition: 50ms linear;
       -o-transition: 50ms linear;
          transition: 50ms linear;
  }

  .chineseButtonWriting{
    color: yellow;
    font-family: "Chinese TakeAway",serif;
    font-size: x-large;
  }

  .dialogButton{
    background-color: black;
  }
  .dialogButtonText{
    color: white;
  }

  @font-face {
    font-family: 'Harakiri';
    src: url('../assets/Harakiri.ttf');
  }

  @font-face {
    font-family: 'Chinese TakeAway';
    src: url('../assets/ChineseTakeaway.ttf');
  }

  @font-face {
    font-family: 'Christmas Flakes';
    src: url('../assets/Flakes.ttf');
  }
  
  @font-face {
    font-family: 'Christmas Wish Monoline';
    src: url('../assets/ChristmasWishMonoline.otf');
  }
  
  @font-face {
    font-family: 'Third Grade';
    src: url('../assets/ThirdGradeHandwriting.ttf');
  }


  h1 {
    display: inline;
    position: relative;
    font: 40px Helvetica, Sans-Serif;
    letter-spacing: -1px;
    color: rgba(0,0,255,0.5);
  }

  h1::after {
    content: "Coming Soon!!";
    white-space: nowrap;
    position: absolute; left: 2px; top: 1px;
    color: rgba(255,0,0,0.5);
  }

.christmasButton {
  visibility: visible;
  display: inline-block;
  -webkit-box-sizing:border-box;
     -moz-box-sizing:border-box;
          box-sizing:border-box;
  min-width:100px;
  padding: 22px 33px;
  font-family: 'Lobster', cursive;
  font-size: 26px;
  line-height: 26px;
  text-decoration: none;
  color: #FFF;
  text-shadow: 0 1px 2px rgba(0,0,0,0.75);
  background: #5e0d0c;
  outline: none;
  border-radius: 15px;
  border: 1px solid #4c0300;
  box-shadow:
    inset 1px 1px 0px rgba(255,255,255,0.25), /* highlight */
    inset 0 0 6px #a23227, /* inner glow */
    inset 0 80px 80px -40px #ac3223, /* gradient */
    1px 1px 3px rgba(0,0,0,0.75); /* shadow */

  position: relative;
  overflow: visible; /* IE9 & 10 */
  -webkit-transition: 500ms linear;
     -moz-transition: 500ms linear;
       -o-transition: 500ms linear;
          transition: 500ms linear;
}

.christmasButton::before {
  content: '';
  display: block;
  position: absolute;
  top: -7px;
  left: -3px;
  right: 0;
  height: 23px;
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAAXCAYAAACS5bYWAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAABFpJREFUeNrUV0tIo1cUvpkYjQ4xxSA6DxuNqG0dtaUKOgs3s6i0dFd3pSsXdjeIixakiGA34sZuXCkoONLFwJTK4GMYLYXg29gatTpiXurkbd7vv9/5ub+IxuhA7eiFQ5Kbc8/57ne/e87/ywRBYLdl3GG3aNwqsLJ0k0tLS+fmcnNzWUVFBVMoFGx2djarvLxcm5OTw+bm5iytra2xc4ExNjY27iqVyvvwK6CpeDzuCYVC1urq6qDA9UcfPp+PHR4esmAwKK6tr68/l5/8rgQ2Ozub1dbWyiYmJooaGxt/VqvV38jlchX9l0qlwoFA4DWS/RKLxRxFRUVf5+XlPcaaT2AP0sVPJBL2SCRiAPBpu93+vKamZo/Ae71eZjabWV1dXVqw7CKwp43ksrCw8Bhg7MJ/PLDZ5PHx8cz29vYT5JGD/bSYLgTrcDgYdk6siSc6NjZWDaAe4ZoHQL+cmZnRpZPnhWDpD8kw7uKo9ML/NMCsd2tr61vkzboMrEyv138M7TyLRqMWMBsX3sMgaZhMpp+AR5EJrCocDpuEGzKg4x8khs+CVWxubvZfR9JkMik4nU7BarUKLpeLmLsKuwIqTLynp4fqmIzASrqQT09Pf1VVVfX0KsWZ6uHBwQHTaDSsoKAgo6/H4xHLEcrVyRwuEisrKzs5XrrIVAVwiUVDKRRrL+YI32ewdVhMApuHWvcj6vids6J2u90MF4yBHUZNgKoEBaRBQalJqFSqtJfUYrGIlQX+ydXVVTN+u0tKSjQNDQ1axJVl2iTypebn55d7e3v/kqoDgZU1NTU9LCws/Py0M+2ekuGincxJ3yF+18jIyHJLS0slQJUWFxczrBeBE0vE5tHRkbixlZWVfSR8gTX/0P5gH7S1tX3Z3t7+BW8qAvwSfr8/jA0EIRM/qoFtampqbW9vTw+XA+ojUruVd3Z2tvb19T2TQFEim81GgVJoCvvj4+NLOJZgaWmpemdn5y3a6BbcnJDAw8HBwac6ne6eqCW5XDwB3qVSqM9/DAwMUNy/eVLabT7sI25qwgujThCBhWE+mAt2yNc4SQKSZrOQQE1HS22VJkmPAGTr7+//fX19fRk+Zgq0trbGeFAKEAQT98BSqKOj47vm5uaa/Px8JeIk4GcaHh6eWlxcfAU/A8xG67BxAX3fwdcbYUpSDJ06Z49Ak8ZC3OL8f3YiA4PBYKdLQ2AJ9OTk5GpXV9cQiCVh79M94QtlPLDUE/1gPNrd3f0W33W4cBoco48zQuy/IZYAMnGqlSc4c66L9JruQUaSARXeT8HGKzxAqFBekni6+h46+pMzGiJGMgTOJh1yU/KNEGDvZWvfBawkA9ppwGg0mrRa7SOI2g+gxOgbJIpdFpj72PnxSnPX8vqRxTURgBQWKisrH+GThOm+CtAzoK/9/Uiqq/6hoaHfdnd3jaOjo7/yY7yxbwqkWy3sQzpS2C6YirwvUJk0y7hurfyGRrnduPGvAAMASmo8wzeVwfsAAAAASUVORK5CYII=) no-repeat 0 0,
  url(data:image/png;base64,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) no-repeat 50% 0,
  url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACEAAAAXCAYAAACFxybfAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAodJREFUeNrsVb1rWlEUv2pN/GqspKRSKFYXWzEloIWif0Fn6dJChQ7OQil0qd3EzcEpg0OgdHDr4CQODk7VRlLMEIVqApX4We0zflR9/Z1Ui4T34ksaaAYP/Hzc673n/M6550PG8zz73yKjn0wm83fDYDAwo9HINBrNnwOQg4MDs0ql2lQqlfdAWont7ng8Pjw+Ps44nc4G1pI9EXWaSOzt7TGO42aH5Pv7+08ajUZ0MBiUeXEZd7vdL5VK5fX29rZ+5tQiEmdxKrlcjsEYczgcynK5/BKKv/IXFNz/XiqVXkHdjUuRIA9SqdRD8or/R8Ez9fr9fqHVakUR4c2z0REjIQuHw2ZcrPBXLCA0RHTezEdHjIQqkUhEr9I4HOILhQLf6/VoOUFEvDMiQiToDx1Cdz+bzZ6bUFarlel0OkkVUK/XWbvdPoVer5fh3ntsfwJ+CJ2XA4p0Op1bpBgJyxDehQQ6nQ5DZXHBYDBZq9V+EhFUndnr9drEqoc2bwJbwGPgtohuVSwWe2Gz2TZMJpNgRKi6qtUqg2EWj8dTgUDgo0KhWPN4PC70EvXOzs67fD6/S6kiRIKeZA1YJ2MiJNbdbvfTUCjkV6vVK2hcDF8GI2w0GrGTkxM2HA5PDxaLxSOfz/cWEfk81X0XIMMFgJJ/srBjCgk8IdcfuVyuZ36//7nFYtkQyAMumUzuRiKRD0jMFLa+AZOpYwqgB/ziBVqmVBKUO7eAB/R0WG/Z7XaTVqtdbTabHJL6EK2djBaBPHA0NSqpbUsiMUeEBgpF4Q5AbZrmSJ/yEWgBTaBNHl9kdkgmMUeG7qwAq9PqovceTA3zlxlgsuswyuXsGsiSxJLEkoSY/BZgAEjRodi+uBruAAAAAElFTkSuQmCC) no-repeat 100% 0;

}
.christmasButton:hover {
  background: #a61715;
  text-shadow: 0 1px 2px rgba(0,0,0,0.75), 0 0 40px #FFF;
  box-shadow:
    inset 1px 1px 0px rgba(255,255,255,0.25), /* highlight */
    inset 0 0 6px #da3b2c, /* inner glow */
    inset 0 80px 80px -40px #dd4330, /* gradient */
    1px 1px 3px rgba(0,0,0,0.75); /* shadow */

}
.christmasButton:focus {
  outline: none; /*FF*/
}
.christmasButton:active {
  box-shadow:
    inset 1px 1px 0px rgba(255,255,255,0.25), /* highlight */
    inset 0 0 6px #da3b2c, /* inner glow */
    inset 0 80px 80px -40px #dd4330, /* gradient */
    0px 1px 0px rgba(255,255,255,0.25); /* shadow */

  -webkit-transition: 50ms linear;
     -moz-transition: 50ms linear;
       -o-transition: 50ms linear;
          transition: 50ms linear;
}

@font-face {
  font-family: 'Lobster';
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.gstatic.com/s/lobster/v23/neILzCirqoswsqX9zoKmMw.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

        .gallery-wrap {
          display: flex;
          flex-direction: row;
          height: 300px;
        }

        .item {
            flex: 1;
            height: 100%;
            background-position: center;
            background-repeat: no-repeat;
            transition: flex 0.8s ease;
            background-size: cover;
            background-image: url("../../backgroundPictures/3.jpg");
        }

        .item:hover{
          flex: 7;
          transform: scale(2);
        }

        .cardBackground1{
          background-image: url('../../backgroundPictures/1.jpg') !important;
        }
        .cardBackground2{
          background-image: url('../../backgroundPictures/2.jpg') !important;
        }
        .cardBackground3{
          background-image: url('../../backgroundPictures/3.jpg') !important;
        }
        .cardBackground4{
          background-image: url('../../backgroundPictures/4.jpg') !important;
        }
        .cardBackground5{
          background-image: url('../../backgroundPictures/5.jpg') !important;
        }
        .cardBackground6{
          background-image: url('../../backgroundPictures/6.jpg') !important;
        }
        .cardBackground7{
          background-image: url('../../backgroundPictures/7.jpg') !important;
        }
        .cardBackground8{
          background-image: url('../../backgroundPictures/8.jpg') !important;
        }.cardBackground9{
          background-image: url('../../backgroundPictures/9.jpg') !important;
        }
         .cardBackground10{
          background-image: url('../../backgroundPictures/10.jpg') !important;
        }
         .cardBackground11{
          background-image: url('../../backgroundPictures/11.jpg') !important;
        }
         .cardBackground12{
          background-image: url('../../backgroundPictures/12.jpg') !important;
        }
         .cardBackground13{
          background-image: url('../../backgroundPictures/13.jpg') !important;
        }
         .cardBackground14{
          background-image: url('../../backgroundPictures/14.jpg') !important;
        }
         .cardBackground15{
          background-image: url('../../backgroundPictures/15.jpg') !important;
        }
         .cardBackground16{
           background-image: url('../../backgroundPictures/16.jpg') !important;
         }
         .cardBackground17{
          background-image: url('../../backgroundPictures/17.jpg') !important;
        }
         .cardBackground18{
          background-image: url('../../backgroundPictures/18.jpg') !important;
        }
         .cardBackground19{
          background-image: url('../../backgroundPictures/19.jpg') !important;
        }
         .cardBackground20{
          background-image: url('../../backgroundPictures/20.jpg') !important;
        }
         .cardBackground21{
          background-image: url('../../backgroundPictures/21.jpg') !important;
        }
         .cardBackground22{
          background-image: url('../../backgroundPictures/22.jpg') !important;
        }
         .cardBackground23{
          background-image: url('../../backgroundPictures/23.jpg') !important;
        }
         .cardBackground24{
          background-image: url('../../backgroundPictures/24.jpg') !important;
        }

        .active{
          border-style: solid;
          border-width: thick;
          border-color: darkblue;
        }

        .deckCell{
          border-radius: 20%;
          margin: 20pt;
          width: 170px;
          height: 220px;
        }

        .alwaysShow{
          color: black;
          background-color: white;
        }

        .textOnCard{
          color: Black;
          font-size: x-large;
          font-weight: bold;
          font-family: "Christmas Wish Monoline",serif;
        }

</style>
