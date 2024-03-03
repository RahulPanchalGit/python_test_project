pipeline {
    agent any
    stages {
        stage('Unittest') {
            steps {
                echo "hello unittest"
                sh '''
                   /usr/bin/python3.7 -m pip install -r requirements.txt
                   /usr/bin/python3.7 -m pytest --cov=. --cov-report xml --flake8 --isort
                '''
                cobertura coberturaReportFile: 'coverage.xml', enableNewApi: true, lineCoverageTargets: '85, 85, 85'
                echo "unittest completed"
            }
        }
        stage('Acceptance') {
            steps {
                echo "deployment to acceptance script to be executed here"
            }
        }
    }
}