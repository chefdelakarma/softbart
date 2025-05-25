#include <string>
#include <ctime>
#include <iomanip>
#include <iostream>

class BigLie {
private:
	std::string WantedAnswer;
	std::string RealAnswer;
	std::string Question;
	std::tm  TimeStamp_RealAnswer;
public:
	BigLie(std::string Question, std::string WantedAnswer)
		: Question(Question), WantedAnswer(WantedAnswer) {}
	std::string SetRealAnswer_GetLie(std::string RealAnswer);
	void SetLie(std::string Question, std::string WantedAnswer);
	void GetTimeStamp();
	std::string GetQuestion();

};
std::string BigLie::SetRealAnswer_GetLie(std::string RealAnswer){
	this->RealAnswer = RealAnswer;
	std::time_t now = std::time(nullptr);
	this->TimeStamp_RealAnswer = *std::localtime(&now);
	return this->WantedAnswer;
}
void BigLie::SetLie(std::string Question, std::string WantedAnswer){
	this->Question = Question;	
	this->WantedAnswer = WantedAnswer;
}
void BigLie::GetTimeStamp(){
    std::cout << std::put_time(&this->TimeStamp_RealAnswer  , "%Y-%m-%d %H:%M:%S") << std::endl;
}
std::string BigLie::GetQuestion(){
	return this->Question;
}

class Sites {
private:
	std::string Url;
	int MaxQuestions, CountQuestions;
	BigLie** Lies;
public:
	Sites(std::string Url, int MaxQuestions);

	~Sites();
	std::string GetUrl();
	void AddLie(std::string Question, std::string WantedAnswer);
	void Interface();
};
Sites::Sites(std::string Url, int MaxQuestions){
		this->Url = Url;
		this->MaxQuestions = MaxQuestions;
		this->Lies = new BigLie*[MaxQuestions];
}

Sites::~Sites(){
	delete[] Lies;
}

std::string Sites::GetUrl(){
	return this->Url;
}
void Sites::AddLie(std::string Question, std::string WantedAnswer){
	while( this->CountQuestions < this->MaxQuestions ){
	Lies[this->CountQuestions++] = new BigLie(Question, WantedAnswer);
}}
void Sites::Interface(){
	std::string Answer;
	std::cout << "URL " << this->Url << std::endl; 
	for (int i=0; i< this->CountQuestions; i++){
	std::cout << "Question " << Lies[i]->GetQuestion() << std::endl;
	std::cout << "Answer" ;
	std::cin >> Answer;
	std::cout << "Lie is " << Lies[i]->SetRealAnswer_GetLie(Answer) << std::endl;
	}
}

int main() {
	Sites mySites[3] = { Sites("http://voorbeeld.com",3), Sites("http://site.com/pagina", 3), Sites("http://voorbeeld.com", 3) };
	for (int i=0; i<3;i++){
		mySites[i].AddLie("toestemming xxx", "waar");
		mySites[i].AddLie("BlaBlaBla", "nietwaar");
		mySites[i].AddLie("cookies", "waar");
	for (int i=0; i < 3; i++){
		mySites[i].Interface();
	}
	}
}

