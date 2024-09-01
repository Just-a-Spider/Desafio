# Problemas Durante el Desarrollo
## Manejar Relaciones en Vistas XML
Durante el desarrollo del módulo, me encontré con dificultades al manejar las relaciones many-to-many, many-to-one y one-to-many dentro de las vistas XML de Odoo. Aunque estoy familiarizado con frameworks como Django REST Framework, la lógica de las vistas en Odoo presentó un nuevo reto.

El modelo de materias (school.subject) tiene una relación many-to-many con los estudiantes y una relación many-to-one con los profesores. Integrar estas relaciones en las vistas formularias fue complejo. Para abordar esto, implementé un notebook que incluye:
- Página de Registro de Estudiantes: Utilicé un árbol/lista de estudiantes existentes para facilitar la selección o registro de nuevos estudiantes.
- Sistema de Calificaciones: Implementé un one-to-many para la gestión de calificaciones.
- Asignación de Profesores: Configuré la vista para asignar el profesor correspondiente a cada materia.
- Este enfoque permitió manejar eficientemente las relaciones complejas en las vistas formularias, garantizando la funcionalidad deseada.

## Manejo de la Seguridad
Durante la implementación del módulo, encontré desafíos al manejar la seguridad, especialmente en la configuración de permisos y accesos. Para abordar esto, trabajé con el archivo ir.model.access.csv, donde comprendí cómo gestionar los accesos de acuerdo a los grupos y permisos, siguiendo el modelo de GitHub proporcionado.

Sin embargo, tuve dificultades al trabajar con el archivo school_security.xml, particularmente al intentar desarrollar categorías y grupos de seguridad. Finalmente, opté por crear dos grupos principales:
- Director de Escuela: Este grupo tiene acceso total al sistema.
- Profesores: Otorgándoles acceso para ingresar calificaciones.
Esta configuración de seguridad asegura que los roles dentro del módulo estén claramente definidos y que los permisos se asignen de manera adecuada según las responsabilidades

# Propuestas Implementadas
Además de los requisitos solicitados, propuse e implementé un sistema de calificaciones individuales para cada curso de los estudiantes. Para esto, desarrollé un modelo adicional llamado Grade, que incluye:
- student_id y subject_id: Ambos conectados mediante relaciones ManyToOne a las tablas de estudiantes y materias, respectivamente.
- grade: Permite registrar la calificación de cada estudiante en cada curso.
Para gestionar las calificaciones, agregué un campo user_id en la tabla de docentes, conectado a la tabla res.users mediante una relación ManyToOne, permitiendo a los profesores calificar a los estudiantes directamente.

En la tabla de estudiantes, propuse dos campos adicionales:
- grade_ids: Conecta al nuevo modelo Grade, permitiendo asociar múltiples calificaciones a un estudiante.
- average_grade: Un campo computado que calcula el promedio de las calificaciones de un estudiante en todos sus cursos mediante la función
- _compute_average_grade. Este promedio incluye también la nota del examen final.

En cuestiones de seguridad:
- Añadí una regla para que los docentes solo puedan ingresar notas de los estudiantes en las materias en las que están vinculados

# Comentarios Adicionales
Este proyecto fue desarrollado en un entorno Linux, lo que hizo que la instalación de Odoo fuera bastante sencilla. Sin embargo, como una propuesta, considero que sería beneficioso crear un tutorial para instalar Odoo utilizando Docker. Esta metodología podría simplificar el proceso de instalación y configuración en distintos entornos, y sería una excelente adición en futuras entrevistas o proyectos.

# Dudas
- ¿Cómo y dónde se realizan los tests dentro de Odoo?
