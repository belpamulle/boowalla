package boowalla.controller

import boowalla.service.getHealth
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get

@Controller("/")
class HealthController {

  @Get("/health")
  fun checkHealth(): String{
    return getHealth()
  }
}