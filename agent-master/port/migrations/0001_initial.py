# Generated by Django 4.2.11 on 2025-06-19 16:10

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='اسم الشركة')),
                ('company_type', models.CharField(choices=[('shipping', 'شحن'), ('transport', 'نقل'), ('logistics', 'لوجستية'), ('commercial', 'تجارية'), ('clearance', 'تخليص'), ('other', 'أخرى')], max_length=20, verbose_name='نوع الشركة')),
                ('registration_number', models.CharField(max_length=50, unique=True, verbose_name='رقم التسجيل')),
                ('tax_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='الرقم الضريبي')),
                ('contact_person', models.CharField(max_length=100, verbose_name='الشخص المسؤول')),
                ('phone_number', models.CharField(max_length=15, verbose_name='رقم الهاتف')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='البريد الإلكتروني')),
                ('address', models.TextField(verbose_name='العنوان')),
                ('city', models.CharField(max_length=100, verbose_name='المدينة')),
                ('country', models.CharField(default='العراق', max_length=100, verbose_name='البلد')),
                ('credit_limit', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='الحد الائتماني (دينار)')),
                ('contract_start_date', models.DateField(verbose_name='تاريخ بداية التعاقد')),
                ('contract_end_date', models.DateField(blank=True, null=True, verbose_name='تاريخ انتهاء التعاقد')),
                ('status', models.CharField(choices=[('active', 'نشط'), ('inactive', 'غير نشط'), ('suspended', 'معلق')], default='active', max_length=20, verbose_name='حالة الشركة')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
            ],
            options={
                'verbose_name': 'شركة',
                'verbose_name_plural': 'شركات',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CompanyTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('income', 'دخل من الشركة'), ('payment', 'دفع للشركة'), ('commission', 'عمولة'), ('service_fee', 'رسوم خدمة'), ('fine', 'غرامة'), ('refund', 'استرداد'), ('advance', 'سلفة')], max_length=20, verbose_name='نوع المعاملة')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='المبلغ (دينار)')),
                ('description', models.TextField(verbose_name='الوصف')),
                ('payment_method', models.CharField(choices=[('cash', 'نقدي'), ('bank_transfer', 'تحويل بنكي'), ('check', 'شيك'), ('mobile', 'موبايل')], max_length=20, verbose_name='طريقة الدفع')),
                ('reference_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='رقم المرجع')),
                ('invoice_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='رقم الفاتورة')),
                ('status', models.CharField(choices=[('pending', 'معلق'), ('completed', 'مكتمل'), ('cancelled', 'ملغي')], default='pending', max_length=20, verbose_name='حالة المعاملة')),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاريخ المعاملة')),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='تاريخ الاستحقاق')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
            ],
            options={
                'verbose_name': 'معاملة مالية مع الشركة',
                'verbose_name_plural': 'معاملات مالية مع الشركات',
                'ordering': ['-transaction_date'],
            },
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_number', models.CharField(max_length=50)),
                ('container_type', models.CharField(choices=[('20DC', '20 قدم عادي'), ('40DC', '40 قدم عادي'), ('20RF', '20 قدم مبرد'), ('40RF', '40 قدم مبرد'), ('TANK', 'صهريج')], max_length=4, verbose_name='نوع الحاوية')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='الوزن (طن)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content_description', models.TextField(blank=True, verbose_name='وصف المحتويات')),
                ('status', models.CharField(choices=[('LOADING', 'تحميل'), ('EMPTY', 'فارغ'), ('GENERAL_CARGO', 'بضائع عامة'), ('UNLOADING', 'تجزئة')], default='LOADING', max_length=20, verbose_name='الحالة')),
                ('size', models.CharField(blank=True, max_length=50, null=True, verbose_name='الحجم')),
            ],
            options={
                'verbose_name': 'الحاوية',
                'verbose_name_plural': 'الحاويات',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='DeliveryOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=50, unique=True, verbose_name='رقم الإذن')),
                ('issue_date', models.DateTimeField(verbose_name='تاريخ الإصدار')),
                ('expiry_date', models.DateTimeField(blank=True, null=True, verbose_name='تاريخ الانتهاء')),
                ('status', models.CharField(choices=[('LOADING', 'تحميل'), ('EMPTY', 'فارغ'), ('GENERAL_CARGO', 'بضائع عامة'), ('UNLOADING', 'تجزئة')], default='LOADING', max_length=20, verbose_name='الحالة')),
                ('notes', models.TextField(blank=True, verbose_name='ملاحظات')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'إذن التسليم',
                'verbose_name_plural': 'أذونات التسليم',
                'ordering': ['-issue_date'],
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم السائق')),
                ('phone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='رقم الهاتف يجب أن يكون 11 رقم', regex='^\\d{11}$')], verbose_name='رقم الهاتف')),
                ('mother_name', models.CharField(max_length=100, verbose_name='اسم الأم')),
                ('governorate', models.CharField(choices=[('BGD', 'بغداد'), ('BSR', 'البصرة'), ('NBL', 'بابل'), ('KRB', 'كربلاء'), ('NJF', 'النجف')], max_length=3, verbose_name='المحافظة')),
                ('is_active', models.BooleanField(default=True, verbose_name='نشط')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('license_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='رقم الرخصة')),
                ('id_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'السائق',
                'verbose_name_plural': 'السائقين',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='DriverFinancialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='الرصيد الحالي (دينار)')),
                ('total_earned', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='إجمالي المكاسب (دينار)')),
                ('total_deducted', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='إجمالي المستقطعات (دينار)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
            ],
            options={
                'verbose_name': 'حساب مالي للسائق',
                'verbose_name_plural': 'حسابات مالية للسائقين',
            },
        ),
        migrations.CreateModel(
            name='DriverTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('payment', 'دفع للسائق'), ('deduction', 'خصم من السائق'), ('bonus', 'مكافأة'), ('fine', 'غرامة'), ('advance', 'سلفة'), ('fuel_allowance', 'بدل وقود'), ('maintenance', 'صيانة')], max_length=20, verbose_name='نوع المعاملة')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='المبلغ (دينار)')),
                ('description', models.TextField(verbose_name='الوصف')),
                ('payment_method', models.CharField(choices=[('cash', 'نقدي'), ('bank_transfer', 'تحويل بنكي'), ('check', 'شيك'), ('mobile', 'موبايل')], max_length=20, verbose_name='طريقة الدفع')),
                ('reference_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='رقم المرجع')),
                ('status', models.CharField(choices=[('pending', 'معلق'), ('completed', 'مكتمل'), ('cancelled', 'ملغي')], default='pending', max_length=20, verbose_name='حالة المعاملة')),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاريخ المعاملة')),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='تاريخ الاستحقاق')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
            ],
            options={
                'verbose_name': 'معاملة مالية مع السائق',
                'verbose_name_plural': 'معاملات مالية مع السائقين',
                'ordering': ['-transaction_date'],
            },
        ),
        migrations.CreateModel(
            name='FinancialReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('drivers_summary', 'ملخص السائقين'), ('companies_summary', 'ملخص الشركات'), ('monthly', 'تقرير شهري'), ('yearly', 'تقرير سنوي'), ('profit_loss', 'الأرباح والخسائر')], max_length=20, verbose_name='نوع التقرير')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان التقرير')),
                ('start_date', models.DateField(verbose_name='تاريخ البداية')),
                ('end_date', models.DateField(verbose_name='تاريخ النهاية')),
                ('total_income', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='إجمالي الدخل (دينار)')),
                ('total_expenses', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='إجمالي المصروفات (دينار)')),
                ('net_profit', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='صافي الربح (دينار)')),
                ('report_data', models.JSONField(default=dict, verbose_name='بيانات التقرير')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
            ],
            options={
                'verbose_name': 'تقرير مالي',
                'verbose_name_plural': 'تقارير مالية',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاريخ البداية')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='تاريخ النهاية')),
                ('status', models.CharField(choices=[('pending', 'قيد الانتظار'), ('active', 'نشط'), ('completed', 'مكتمل'), ('cancelled', 'ملغي')], default='pending', max_length=20, verbose_name='الحالة')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('driver_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='اسم السائق')),
                ('truck_plate', models.CharField(blank=True, max_length=50, null=True, verbose_name='رقم لوحة الشاحنة')),
            ],
            options={
                'verbose_name': 'رحلة',
                'verbose_name_plural': 'رحلات',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='المعرف')),
                ('plate_number', models.CharField(max_length=20, unique=True, verbose_name='رقم اللوحة')),
                ('governorate', models.CharField(choices=[('BGD', 'بغداد'), ('NNW', 'نينوى'), ('BSR', 'البصرة'), ('SLY', 'السليمانية'), ('ARB', 'أربيل'), ('THQ', 'ذي قار'), ('NBL', 'بابل'), ('ANB', 'الأنبار'), ('DIY', 'ديالى'), ('KRK', 'كركوك'), ('NJF', 'النجف'), ('WST', 'واسط'), ('QDS', 'القادسية'), ('SLH', 'صلاح الدين'), ('KRB', 'كربلاء'), ('MSN', 'ميسان'), ('DHK', 'دهوك'), ('MTH', 'المثنى')], max_length=50, verbose_name='المحافظة')),
                ('truck_type', models.CharField(choices=[('FLAT', 'مسطحة'), ('CONT', 'حاويات'), ('TANK', 'صهريج')], max_length=50, verbose_name='نوع الشاحنة')),
                ('is_active', models.BooleanField(default=True, verbose_name='نشط')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'شاحنة',
                'verbose_name_plural': 'الشاحنات',
                'ordering': ['-created_at'],
            },
        ),
    ]
