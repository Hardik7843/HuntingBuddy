from label_studio import labeling_app

# Define sample HTML data
html_data = [
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sample HTML</title>
    </head>
    <body>
        <h1>John works at XYZ Corp in New York as a Software Engineer.</h1>
        <p>Alice is a Data Scientist at ABC Corp in San Francisco.</p>
    </body>
    </html>
    """
]

# Configure Label Studio project with HTML data and annotation template
project_config = {
    "task": {
        "data": html_data,
        "data_type": "html",
        "annotation": {
            "label": "html-entity-recognition",
            "labels": ["Person", "Company", "Location"]
        }
    }
}

# Initialize Label Studio labeling app with project configuration
labeling_app.initialize(project_config)

# Run Label Studio labeling app
labeling_app.run(port=8080, use_anonymous=False)
