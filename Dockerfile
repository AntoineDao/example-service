# Use the official Python image.
# https://hub.docker.com/_/python
FROM python

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

# Install production dependencies.
RUN pip install Flask

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV FLASK_PORT 8080

# Run the web service on container startup.
CMD ["flask", "run", "-p", "$FLASK_PORT"]