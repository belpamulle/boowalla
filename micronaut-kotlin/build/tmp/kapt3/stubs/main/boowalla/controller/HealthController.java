package boowalla.controller;

import java.lang.System;

@kotlin.Metadata(mv = {1, 1, 16}, bv = {1, 0, 3}, k = 1, d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\b\u0007\u0018\u00002\u00020\u0001B\u0005\u00a2\u0006\u0002\u0010\u0002J\b\u0010\u0003\u001a\u00020\u0004H\u0007\u00a8\u0006\u0005"}, d2 = {"Lboowalla/controller/HealthController;", "", "()V", "checkHealth", "", "micronaut-kotlin"})
@io.micronaut.http.annotation.Controller(value = "/")
public final class HealthController {
    
    @org.jetbrains.annotations.NotNull()
    @io.micronaut.http.annotation.Get(value = "/health")
    public final java.lang.String checkHealth() {
        return null;
    }
    
    public HealthController() {
        super();
    }
}