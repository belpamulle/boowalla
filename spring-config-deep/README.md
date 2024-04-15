# Getting Started

### Reference Documentation

https://start.spring.io/

![dependency.png](docs%2Fdependency.png)

see in [build.gradle](build.gradle)
```
dependencies {
implementation 'org.springframework.cloud:spring-cloud-config-server'
}
```

If you're using the git profile, you need to specify a Git URI in your configuration. If you've set spring.cloud.config.server.bootstrap=true, you need to use a composite configuration.

Here's an example of how you can set the Git URI in your application.properties or application.yml file:
 in application.yml:

```
spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/yourusername/config-repo
```

Replace https://github.com/yourusername/config-repo with the actual URI of your Git repository.

If you've set spring.cloud.config.server.bootstrap=true, you need to use a composite configuration like this:

```
spring:
  cloud:
    config:
      server:
        bootstrap: true
        composite:
        - type: git
          uri: https://github.com/yourusername/config-repo
        - type: native
          search-locations: file:/etc/config-repo
```
______________

If you want to use native (local) configuration only, you need to specify that in your application.properties or application.yml file.

Here's how you can do it:

in application.yml:

```
spring:
  profiles:
    active: native
  cloud:
    config:
      server:
        native:
          searchLocations: file:/path/to/your/config/files

```
Replace `file:/path/to/your/config/files` with the actual path to your local configuration files.

After making these changes, restart your application. It should now use the local file system for configuration data.