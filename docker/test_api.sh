#!/bin/bash

BASE_URL="http://localhost:5001"

# Créer une nouvelle tâche (POST)
echo "Creating a new task..."
create_response=$(curl -s -X POST $BASE_URL/tasks \
  -H "Content-Type: application/json" \
  -d '{"description": "Apprendre Flask", "frequency": "daily"}')
echo "Response: $create_response"
echo

# Récupérer toutes les tâches (GET)
echo "Getting all tasks..."
get_response=$(curl -s $BASE_URL/tasks)
echo "Response: $get_response"
echo

# Extraire l'ID de la première tâche pour les tests de mise à jour et de suppression
task_id=$(echo $get_response | jq -r '.[0].id')
echo "Task ID to update and delete: $task_id"
echo

# Mettre à jour une tâche (PUT)
echo "Updating the task..."
update_response=$(curl -s -X PUT $BASE_URL/tasks/$task_id \
  -H "Content-Type: application/json" \
  -d '{"description": "Maîtriser Flask", "frequency": "yearly"}')
echo "Response: $update_response"
echo

# Supprimer une tâche (DELETE)
echo "Deleting the task..."
delete_response=$(curl -s -X DELETE $BASE_URL/tasks/$task_id)
echo "Response: $delete_response"
echo
