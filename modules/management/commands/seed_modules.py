from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from modules.models import Module, Registration
from students.models import Student
import random


class Command(BaseCommand):
    help = 'Seed the database with sample modules and registrations'

    def add_arguments(self, parser):
        parser.add_argument(
            '--modules-only',
            action='store_true',
            help='Only create modules, skip registrations',
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing modules before seeding',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('🗑️  Clearing existing modules...')
            Module.objects.all().delete()
            Registration.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('✅ Existing modules cleared'))

        self.stdout.write('🚀 Starting modules database seeding...')
        self.stdout.write('=' * 50)

        # Create modules
        self.stdout.write('\n📚 Creating sample modules...')
        modules = self.create_sample_modules()
        self.stdout.write(f'✅ Created {len(modules)} modules')

        if not options['modules_only']:
            # Create registrations
            self.stdout.write('\n📝 Creating sample registrations...')
            registrations_count = self.create_sample_registrations(modules=modules)

        self.stdout.write('\n' + '=' * 50)
        self.stdout.write('🎉 Modules database seeding completed!')
        self.stdout.write(f'📊 Summary:')
        self.stdout.write(f'   - Modules: {Module.objects.count()}')
        self.stdout.write(f'   - Registrations: {Registration.objects.count()}')
        self.stdout.write(f'   - Students: {Student.objects.count()}')

        # Show some statistics
        self.stdout.write(f'\n📈 Module Statistics:')
        for category in ['core', 'elective', 'optional', 'prerequisite']:
            count = Module.objects.filter(category=category).count()
            self.stdout.write(f'   - {category.title()}: {count} modules')

        self.stdout.write(f'\n🎯 Registration Statistics:')
        for module in Module.objects.all()[:5]:  # Show first 5 modules
            reg_count = module.registered_students_count
            available = module.available_spots
            self.stdout.write(f'   - {module.code}: {reg_count}/{module.max_students} students ({available} spots available)')

    def create_sample_modules(self):
        """Create sample modules in the database"""
        sample_modules = [
            # Computer Science Core Modules
            {
                'name': 'Introduction to Computer Science',
                'code': 'CS101',
                'credit': 3,
                'category': 'core',
                'description': 'Fundamental concepts of computer science including programming basics, algorithms, and data structures. Covers Python programming, problem-solving techniques, and computational thinking.',
                'max_students': 30,
                'availability': True
            },
            {
                'name': 'Programming Fundamentals',
                'code': 'CS102',
                'credit': 4,
                'category': 'core',
                'description': 'Advanced programming concepts including object-oriented programming, data structures, and algorithm analysis. Students will work with Java and C++.',
                'max_students': 25,
                'availability': True
            },
            {
                'name': 'Data Structures and Algorithms',
                'code': 'CS201',
                'credit': 4,
                'category': 'core',
                'description': 'Study of fundamental data structures (arrays, linked lists, trees, graphs) and algorithms (sorting, searching, graph traversal).',
                'max_students': 25,
                'availability': True
            },
            {
                'name': 'Database Management Systems',
                'code': 'CS202',
                'credit': 3,
                'category': 'core',
                'description': 'Comprehensive study of database design, SQL, normalization, and database administration. Covers both relational and NoSQL databases.',
                'max_students': 25,
                'availability': True
            },
            {
                'name': 'Software Engineering',
                'code': 'CS301',
                'credit': 3,
                'category': 'core',
                'description': 'Software development lifecycle, design patterns, testing, and project management. Includes agile methodologies and DevOps practices.',
                'max_students': 30,
                'availability': True
            },
            
            # Computer Science Elective Modules
            {
                'name': 'Web Development',
                'code': 'CS401',
                'credit': 3,
                'category': 'elective',
                'description': 'Modern web development techniques using HTML, CSS, JavaScript, and popular frameworks like React and Node.js.',
                'max_students': 20,
                'availability': True
            },
            {
                'name': 'Mobile App Development',
                'code': 'CS402',
                'credit': 3,
                'category': 'elective',
                'description': 'Development of mobile applications for iOS and Android platforms using React Native and Flutter.',
                'max_students': 15,
                'availability': True
            },
            {
                'name': 'Machine Learning',
                'code': 'CS403',
                'credit': 4,
                'category': 'elective',
                'description': 'Fundamentals of machine learning algorithms, supervised and unsupervised learning, neural networks, and deep learning.',
                'max_students': 20,
                'availability': True
            },
            {
                'name': 'Artificial Intelligence',
                'code': 'CS404',
                'credit': 4,
                'category': 'elective',
                'description': 'Introduction to AI concepts including search algorithms, knowledge representation, and natural language processing.',
                'max_students': 18,
                'availability': True
            },
            {
                'name': 'Computer Networks',
                'code': 'CS405',
                'credit': 3,
                'category': 'elective',
                'description': 'Network protocols, architecture, security, and administration. Covers TCP/IP, routing, and network management.',
                'max_students': 22,
                'availability': True
            },
            
            # Data Science Modules
            {
                'name': 'Data Analytics',
                'code': 'DS101',
                'credit': 3,
                'category': 'elective',
                'description': 'Introduction to data analysis, statistical methods, and data visualization techniques using Python and R.',
                'max_students': 25,
                'availability': True
            },
            {
                'name': 'Big Data Processing',
                'code': 'DS201',
                'credit': 4,
                'category': 'elective',
                'description': 'Processing and analysis of large-scale datasets using Hadoop, Spark, and distributed computing techniques.',
                'max_students': 20,
                'availability': True
            },
            {
                'name': 'Data Visualization',
                'code': 'DS301',
                'credit': 3,
                'category': 'elective',
                'description': 'Creating effective data visualizations and dashboards using tools like Tableau, D3.js, and Python libraries.',
                'max_students': 18,
                'availability': True
            },
            
            # Cybersecurity Modules
            {
                'name': 'Cybersecurity Fundamentals',
                'code': 'CYB101',
                'credit': 3,
                'category': 'optional',
                'description': 'Introduction to cybersecurity concepts, threats, and protection mechanisms. Covers ethical hacking and security best practices.',
                'max_students': 25,
                'availability': True
            },
            {
                'name': 'Network Security',
                'code': 'CYB201',
                'credit': 3,
                'category': 'optional',
                'description': 'Advanced network security concepts including firewalls, intrusion detection, VPNs, and secure network design.',
                'max_students': 20,
                'availability': True
            },
            {
                'name': 'Cryptography',
                'code': 'CYB301',
                'credit': 3,
                'category': 'optional',
                'description': 'Mathematical foundations of cryptography, encryption algorithms, digital signatures, and cryptographic protocols.',
                'max_students': 18,
                'availability': True
            },
            
            # Business and Management Modules
            {
                'name': 'Digital Marketing',
                'code': 'MKT101',
                'credit': 2,
                'category': 'optional',
                'description': 'Digital marketing strategies, social media marketing, SEO, content marketing, and online advertising techniques.',
                'max_students': 30,
                'availability': True
            },
            {
                'name': 'Project Management',
                'code': 'PM101',
                'credit': 2,
                'category': 'optional',
                'description': 'Project planning, execution, monitoring, and risk management principles. Covers both traditional and agile methodologies.',
                'max_students': 35,
                'availability': True
            },
            {
                'name': 'Business Analytics',
                'code': 'BA101',
                'credit': 3,
                'category': 'optional',
                'description': 'Using data analytics to make business decisions. Covers statistical analysis, forecasting, and business intelligence tools.',
                'max_students': 25,
                'availability': True
            },
            
            # Prerequisite Modules
            {
                'name': 'Mathematics for Computing',
                'code': 'MATH101',
                'credit': 3,
                'category': 'prerequisite',
                'description': 'Essential mathematics for computer science including discrete mathematics, linear algebra, and calculus.',
                'max_students': 40,
                'availability': True
            },
            {
                'name': 'Statistics and Probability',
                'code': 'STAT101',
                'credit': 3,
                'category': 'prerequisite',
                'description': 'Fundamental concepts of statistics and probability theory essential for data science and machine learning.',
                'max_students': 35,
                'availability': True
            },
            {
                'name': 'English for Academic Purposes',
                'code': 'ENG101',
                'credit': 2,
                'category': 'prerequisite',
                'description': 'Academic writing, research skills, and presentation techniques for university-level coursework.',
                'max_students': 50,
                'availability': True
            }
        ]

        created_modules = []
        
        for module_data in sample_modules:
            module, created = Module.objects.get_or_create(
                code=module_data['code'],
                defaults=module_data
            )
            if created:
                self.stdout.write(f"✅ Created module: {module.name} ({module.code})")
            else:
                self.stdout.write(f"ℹ️  Module already exists: {module.name} ({module.code})")
            
            created_modules.append(module)
        
        return created_modules

    def create_sample_registrations(self, students=None, modules=None):
        """Create sample registrations between students and modules"""
        if not students:
            students = Student.objects.all()
        
        if not modules:
            modules = Module.objects.all()
        
        if not students.exists():
            self.stdout.write(self.style.WARNING("⚠️  No students found. Please create students first."))
            return 0
        
        if not modules.exists():
            self.stdout.write(self.style.WARNING("⚠️  No modules found. Please create modules first."))
            return 0
        
        registrations_created = 0
        
        for student in students:
            # Each student registers for 3-6 random modules
            num_modules = random.randint(3, 6)
            available_modules = [m for m in modules if m.availability and not m.is_full]
            
            if len(available_modules) < num_modules:
                num_modules = len(available_modules)
            
            if num_modules > 0:
                selected_modules = random.sample(available_modules, num_modules)
                
                for module in selected_modules:
                    registration, created = Registration.objects.get_or_create(
                        student=student,
                        module=module
                    )
                    if created:
                        registrations_created += 1
                
                self.stdout.write(f"📚 Created {len(selected_modules)} registrations for {student.user.get_full_name()}")
        
        self.stdout.write(f"🎯 Total registrations created: {registrations_created}")
        return registrations_created
