package com.belpamulle.spring;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.config.server.EnableConfigServer;

@SpringBootApplication
@EnableConfigServer
public class SpringConfigDeepApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringConfigDeepApplication.class, args);
	}

}
