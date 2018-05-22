#!flask/bin/python
from flask import Flask, jsonify, abort, make_response
import csv

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    response = make_response("Erro 404: Nao Encontrado" + '\n')
    response.mimetype = 'text/csv'
    return response


# Numero de publicacoes em uma determinada conferencia de uma area

@app.route('/api/<string:field>/<string:conference>/papers/total', methods=['GET'])
def papers_conference_total(field,conference):

    try:
        with open ('data/' + field + '-out-confs.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            output = ""

            for line in csv_reader:
                if(line[0] == conference):
                    output += line[1] + '\n'
                    response = make_response(output)
                    response.mimetype = 'text/csv'
                    return response
                else:
                    return not_found(404)


    except IOError:
        return not_found(404)

# Numero de publicacoes no conjunto de conferencias de uma area

@app.route('/api/<string:field>/papers/total', methods=['GET'])
def papers_field_total(field):

    try:
        with open ('data/' + field + '-out-confs.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            output = ""
            total = 0

            for line in csv_reader:
                total += int(line[1])

            output = str(total)

            response = make_response(output + '\n')
            response.mimetype = 'text/csv'
            return response

    except IOError:
        return not_found(404)

# Scores de todos os departamentos em uma area

@app.route('/api/<string:field>/scores', methods=['GET'])
def scores_field(field):

    try:
        with open ('data/' + field + '-out-scores.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            output = ""

            for line in csv_reader:
                output += ','.join(line)+ '\n'

            response = make_response(output)
            response.mimetype = 'text/csv'
            return response

    except IOError:
        return not_found(404)

#Score de um determinado departamento em uma area.

@app.route('/api/<string:field>/<string:department>/scores', methods=['GET'])
def scores_department(field,department):

    try:
        with open ('data/' + field + '-out-scores.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            output = ""

            for line in csv_reader:
                if(line[0] == department):
                    output = line[1] + '\n'
                    response = make_response(output)
                    response.mimetype = 'text/csv'
                    return response
                else:
                    return not_found(404)

    except IOError:
        return not_found(404)


# Numero de professores que publicam em uma determinada area (organizados por departamentos)

@app.route('/api/professors/<string:field>/total', methods=['GET'])
def professors_total(field):

    try:
        with open ('data/' + field + '-researchers.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            output = ""
            department_count = {}

            for line in csv_reader:
                department_count[line[1]] = department_count.get(line[1],0) + 1

            for count in department_count:
                output += str(count) + ',' + str(department_count[count]) + '\n'

            response = make_response(output)
            response.mimetype = 'text/csv'
            return response

    except IOError:
        return not_found(404)

# Numero de professores de um determinado departamento que publicam em uma area

@app.route('/api/professors/<string:field>/<string:department>/total', methods=['GET'])
def professors_dep_total(field,department):

    try:
        with open ('data/' + field + '-researchers.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            output = ""
            total = 0

            for line in csv_reader:
                if line[1] == department:
                    total += 1

            output = str(total) + '\n'

            response = make_response(output)
            response.mimetype = 'text/csv'
            return response

    except IOError:
        return not_found(404)


# Todos os papers de uma area (ano, titulo, deptos e autores)

@app.route('/api/<string:field>/papers', methods=['GET'])
def papers_field(field):

    try:
        with open ('data/' + field + '-out-papers.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            output = ""

            for line in csv_reader:
                output += line[0] + ',' +  line[2]+ ',' + line[3] + ',' + line[4] +'\n'

            response = make_response(output)
            response.mimetype = 'text/csv'
            return response

    except IOError:
        return not_found(404)

# Todos os papers de uma area em um determinado ano


@app.route('/api/<string:field>/papers/<string:year>', methods=['GET'])
def papers_field_year(field,year):

    try:
        with open ('data/' + field + '-out-papers.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            output = ""

            for line in csv_reader:
                if(line[0] == year):
                    output +=   line[2]+ ',' + line[3]+ ',' + line[4]  + '\n'

            if(output == ""):
                return not_found(404)
            response = make_response(output)
            response.mimetype = 'text/csv'
            return response

    except IOError:
        return not_found(404)

# Todos os papers de um departamento em uma area

@app.route('/api/<string:field>/<string:department>/papers', methods=['GET'])
def papers_field_dep(field,department):

    try:
        with open ('data/' + field + '-out-papers.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            output = ""

            for line in csv_reader:
                if(line[3] == department):
                    output +=   line[0]+ ',' + line[2]+ ',' + line[4]  + '\n'

            if(output == ""):
                return not_found(404)

            response = make_response(output)
            response.mimetype = 'text/csv'
            return response

    except IOError:
        return not_found(404)

# Todos os papers de um professor (dado o seu nome)

@app.route('/api/professors/<string:professor>/papers', methods=['GET'])
def papers_professor(professor):

    try:
        with open ('data/profs/search/' + professor + '.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            output = ""

            for line in csv_reader:
                output += ','.join(line)+ '\n'

            response = make_response(output)
            response.mimetype = 'text/csv'
            return response

    except IOError:
        return not_found(404)

if __name__ == '__main__':
    app.run(debug=True)