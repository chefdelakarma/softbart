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
	std::string Url;
public:
	BigLie(std::string Url, std::string Question, std::string WantedAnswer)
		: Url(Url), Question(Question), WantedAnswer(WantedAnswer) {}
	std::string SetRealAnswer_GetLie(std::string RealAnswer);
	void GetTimeStamp();
	std::string GetUrl();
};
std::string BigLie::SetRealAnswer_GetLie(std::string RealAnswer){
	this->RealAnswer = RealAnswer;
	std::time_t now = std::time(nullptr);
	this->TimeStamp_RealAnswer = *std::localtime(&now);
	return this->WantedAnswer;
}
void BigLie::GetTimeStamp(){
    std::cout << std::put_time(&this->TimeStamp_RealAnswer  , "%Y-%m-%d %H:%M:%S") << std::endl;
}
std::string BigLie::GetUrl(){
	return this->Url;
}
int main() {

	BigLie myBigLie[3] = { BigLie("http://voorbeeld.com","cookies", "waar"), BigLie("http://site.com/pagina","toestemming xxx", "waar"), BigLie("http://voorbeeld.com","BlaBlaBla", "nietwaar")};

	for (int i=0; i<3;i++){
		std::cout << "Lie " << myBigLie[i].SetRealAnswer_GetLie("False") << std::endl;
		std::cout << "url " << myBigLie[i].GetUrl() << std::endl;
		std::cout << "Time " << myBigLie[i].GetTimeStamp();
	}
}

