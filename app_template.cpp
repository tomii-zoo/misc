#include <iostream>
#include <unistd.h>

class App {
public:
	bool is_run = true;
	int frame = 0;

	App() { std::cout << "start" << std::endl; }
	void run() {
	  std::cout << frame++ << std::endl;
	  sleep(1);
	}
	int quit() { return 0; }
};

int main() {
  App app;
  
  while (app.is_run) {
	  app.run();
  }

  return app.quit();
}
