from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from schedule.models import *

from django.db.models import Model, BooleanField, CharField, IntegerField, DateField, DateTimeField, DecimalField, ForeignKey, EmailField
# import psycopg2.extension
from bsct.models import BSCTModelMixin
from schedule.models.calendars import CalendarManager
from Projetweb.utils import *

level_uni = (('L1', ('L1')), ('L2', ('L2')),
             ('L3', ('L3')), ('M1', ('M1')), ('M2', ('M2')))
semestre_uni = (('S1', ('S1')), ('S2', ('S2')), ('S3', ('S3')), ('S4', ('S4')),
                ('S5', ('S5')), ('S6', ('S6')), ('S7', ('S7')), ('S8', ('S8')), ('S9', ('S9')), ('S10', ('S10')))
statut_prof_uni = (('Professeur des universités', ('Professeur des universités')),
                   ('Maître de conférences', ('Maître de conférences')))


# Create your models here.
class Professeur(BSCTModelMixin, models.Model):
    # Classe de Professeur.
    # BSCTModelMixin permet de ne pas écrire les méthodes get_absolute_url, get_delete_url...
    # Doc :
    # * https://pypi.org/project/django-bootstrap-crud-templates/
    # Exemple :
    # * https://github.com/Alem/django-bootstrap-crud-templates/blob/master/demo/crud/models.py

    # attribut entre "" est le verbose name qui nous servira au moment des affichages

    num_professeur = models.AutoField("Numéro du professeur", primary_key=True)
    prenom = models.CharField("Prénom du professeur", max_length=30)
    nom = models.CharField("Nom du professeur", max_length=30)
    adresse_courriel = models.EmailField("Son adresse courriel", max_length=60)
    date_naissance = models.DateField("Sa date de naissance")
    statut = models.CharField(
        "Son statut au sein de la fac", max_length=30, choices=statut_prof_uni)
    experience = models.IntegerField("Ses années d'expériences")

    # La redéfinition de __str__ permet de changer le titre de la page détail
    def __str__(self):
        return self.prenom + ' ' + self.nom

    # Précise le nom à donner à la table - permet les majuscules donc plus jojo
    class Meta:
        verbose_name = "Professeur"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['prenom', 'nom', 'adresse_courriel', 'date_naissance', 'statut', 'experience']


class Etudiant(BSCTModelMixin, models.Model):
    num_etudiant = models.AutoField("Numéro de l'étudiant", primary_key=True)
    prenom = models.CharField("Prénom de l'étudiant", max_length=30)
    nom = models.CharField("Nom de l'étudiant", max_length=30)
    adresse_courriel = models.EmailField("Son adresse courriel", max_length=60)
    date_naissance = models.DateField("Sa date naissance")
    niveau = models.CharField(
        "Son niveau universitaire", max_length=2, choices=level_uni, default=None)
    fk_groupe = models.ForeignKey(
        "Groupe", verbose_name="Groupe", on_delete=models.CASCADE)

    def __str__(self):
        return self.prenom + ' ' + self.nom

    class Meta:
        verbose_name = "Etudiant"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['prenom', 'nom', 'adresse_courriel', 'date_naissance', 'niveau', 'fk_groupe']


class UC(BSCTModelMixin, models.Model):
    id_uc = models.AutoField("Identifiant de l'UC", primary_key=True)
    nom_matiere = models.CharField(
        "Nom de la matière", max_length=30, default=' ')
    ects = models.FloatField("Son coefficient")
    type_uc = models.CharField("Domaine de l'UC", max_length=15)
    semestre = models.CharField(
        "A quelle semestre appartient-il?", max_length=3, choices=semestre_uni)
    fk_formation = models.ForeignKey(
        "Formation", verbose_name="Formation", on_delete=models.CASCADE)  # clés multiples

    def __str__(self):
        return self.nom_matiere

    class Meta:
        verbose_name = "UC"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['nom_matiere', 'ects', 'type_uc', 'semestre', 'fk_formation']


'''déploiement rapide
class UE(BSCTModelMixin, models.Model):
    id_ue = models.AutoField("Identifiant de l'UE", primary_key=True)
    nom_ue = models.CharField("Nom de la matière", max_length=30, default=' ')
    semestre = models.CharField(
        "A quelle semestre appartient-il?", max_length=3, choices=semestre_uni)
    fk_formation = models.ForeignKey(
        "Formation", verbose_name="Formation", on_delete=models.CASCADE)  # clés multiples

    def __str__(self):
        return self.nom_ue

    class Meta:
        verbose_name = "UE"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['nom_ue', 'fk_formation']
'''


class Salle(BSCTModelMixin, models.Model):
    id_salle = models.AutoField("Identifiant de la salle", primary_key=True)
    code = models.CharField("Nom de la salle", max_length=100)
    batiment = models.CharField("Dans quel bâtiment?", max_length=100)
    capacite = models.IntegerField("Sa capacité")
    nb_pc = models.IntegerField("Le nombre de PCs dans la salle")
    projecteur = models.IntegerField("Le nombre de projecteurs")
    tableaux = models.IntegerField("Le nombre de tableaux?")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Salle"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['code', 'batiment', 'capacite', 'nb_pc', 'projecteur', 'tableaux']


class Groupe(BSCTModelMixin, models.Model):
    id_groupe = models.AutoField("Identifiant du groupe", primary_key=True)
    libelle = models.CharField("Nom du groupe", max_length=100)
    niveau = models.CharField(
        "Niveau du groupe", max_length=2, choices=level_uni)
    fk_formation = models.ForeignKey(
        "Formation", verbose_name="Formation", on_delete=models.CASCADE)  # clés multiples

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name = "Groupe"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['libelle', 'niveau']


class Formation(BSCTModelMixin, models.Model):
    id_formation = models.AutoField(
        "Identifiant de la formation", primary_key=True)
    nom_formation = models.CharField("Nom de la formation", max_length=100)
    ufr_rattachement = models.CharField(
        "UFR de rattachement", max_length=100, default='SEGMI')

    def __str__(self):
        return self.nom_formation

    class Meta:
        verbose_name = "Formation"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['nom_formation', 'ufr_rattachement']


class Seance(BSCTModelMixin, models.Model):
    id_seance = models.AutoField(
        "Identifiant de la séance", primary_key=True)
    timecode_debut = models.DateTimeField(
        "Date et heure de début de la séance")
    timecode_fin = models.DateTimeField(
        "Date et heure de fin de la séance")
    fk_professeur = models.ForeignKey(
        Professeur, verbose_name="Professeur en charge de la séance", on_delete=models.CASCADE)
    fk_groupe = models.ForeignKey(
        Groupe, verbose_name="Groupe assistant à la séance", on_delete=models.CASCADE)
    fk_uc = models.ForeignKey(
        UC, verbose_name="Matière de la séance", on_delete=models.CASCADE, default=None)
    fk_salle = models.ForeignKey(
        Salle, verbose_name="Dans quelle salle se déroule-t-elle?", on_delete=models.CASCADE)
    calendrier = models.ForeignKey(
        'SeanceCalendrier', on_delete=models.CASCADE, verbose_name=("A quel calendrier l'ajouter?")
    )

    class Meta:
        verbose_name = "Séance"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['timecode_debut', 'timecode_fin', 'fk_professeur', 'fk_groupe', 'fk_uc', 'fk_salle']

    def __str__(self):
        return gettext("%(id)s: %(timecode_debut)s - %(timecode_fin)s") % {
            'id': self.id_seance,
            'timecode_debut': date(self.timecode_debut, django_settings.DATE_FORMAT),
            'timecode_fin': date(self.timecode_fin, django_settings.DATE_FORMAT),
        }

    @property
    def seconds(self):
        return (self.timecode_fin - self.timecode_debut).total_seconds()

    @property
    def minutes(self):
        return float(self.seconds) / 60

    @property
    def hours(self):
        return float(self.seconds) / 3600

    def get_absolute_url(self):
        return reverse('event', args=[self.id_seance])

    def get_occurrences(self, start, end, clear_prefetch=True):
        if clear_prefetch:
            self.occurrence_set._remove_prefetched_objects()

        persisted_occurrences = self.occurrence_set.all()
        occ_replacer = SeanceOccurrenceReplacer(persisted_occurrences)
        occurrences = self._get_occurrence_list(start, end)
        final_occurrences = []
        for occ in occurrences:
            # replace occurrences with their persisted counterparts
            if occ_replacer.has_occurrence(occ):
                p_occ = occ_replacer.get_occurrence(occ)
                # ...but only if they are within this period
                if p_occ.start < end and p_occ.end >= start:
                    final_occurrences.append(p_occ)
            else:
                final_occurrences.append(occ)
        # then add persisted occurrences which originated outside of this period but now
        # fall within it
        final_occurrences += occ_replacer.get_additional_occurrences(
            start, end)
        return final_occurrences

    def get_rrule_object(self, tzinfo):
        if self.rule is None:
            return
        params = self._event_params()
        frequency = self.rule.rrule_frequency()
        if timezone.is_naive(self.timecode_debut):
            dtstart = self.timecode_debut
        else:
            dtstart = tzinfo.normalize(
                self.timecode_debut).replace(tzinfo=None)

        if self.end_recurring_period is None:
            until = None
        elif timezone.is_naive(self.end_recurring_period):
            until = self.end_recurring_period
        else:
            until = tzinfo.normalize(
                self.end_recurring_period.astimezone(tzinfo)
            ).replace(tzinfo=None)

        return rrule.rrule(frequency, dtstart=dtstart, until=until, **params)

    def _create_occurrence(self, start, end=None):
        if end is None:
            end = start + (self.timecode_fin - self.timecode_debut)
        return SeanceOccurence(
            seance=self, start=start, end=end, original_start=start, original_end=end
        )

    def get_occurrence(self, date):
        use_naive = timezone.is_naive(date)
        tzinfo = timezone.utc
        if timezone.is_naive(date):
            date = timezone.make_aware(date, timezone.utc)
        if date.tzinfo:
            tzinfo = date.tzinfo
        rule = self.get_rrule_object(tzinfo)
        if rule:
            next_occurrence = rule.after(
                tzinfo.normalize(date).replace(tzinfo=None), inc=True
            )
            next_occurrence = tzinfo.localize(next_occurrence)
        else:
            next_occurrence = self.timecode_debut
        if next_occurrence == date:
            try:
                return 'SeanceOccurrence'.objects.get(event=self, original_start=date)
            except Occurrence.DoesNotExist:
                if use_naive:
                    next_occurrence = timezone.make_naive(
                        next_occurrence, tzinfo)
                return self._create_occurrence(next_occurrence)

    def _get_occurrence_list(self, start, end):
        if self.rule is not None:
            duration = self.timecode_fin - self.timecode_debut
            use_naive = timezone.is_naive(start)

            # Use the timezone from the start date
            tzinfo = timezone.utc
            if start.tzinfo:
                tzinfo = start.tzinfo

            # Limit timespan to recurring period
            occurrences = []
            if self.end_recurring_period and self.end_recurring_period < end:
                end = self.end_recurring_period

            start_rule = self.get_rrule_object(tzinfo)
            start = start.replace(tzinfo=None)
            if timezone.is_aware(end):
                end = tzinfo.normalize(end).replace(tzinfo=None)

            o_starts = []

            # Occurrences that start before the timespan but ends inside or after timespan
            closest_start = start_rule.before(start, inc=False)
            if closest_start is not None and closest_start + duration > start:
                o_starts.append(closest_start)

            # Occurrences starts that happen inside timespan (end-inclusive)
            occs = start_rule.between(start, end, inc=True)
            # The occurrence that start on the end of the timespan is potentially
            # included above, lets remove if thats the case.
            if len(occs) > 0:
                if occs[-1] == end:
                    occs.pop()
            # Add the occurrences found inside timespan
            o_starts.extend(occs)

            # Create the Occurrence objects for the found start dates
            for o_start in o_starts:
                o_start = tzinfo.localize(o_start)
                if use_naive:
                    o_start = timezone.make_naive(o_start, tzinfo)
                o_end = o_start + duration
                occurrence = self._create_occurrence(o_start, o_end)
                if occurrence not in occurrences:
                    occurrences.append(occurrence)
            return occurrences
        else:
            # check if event is in the period
            if self.timecode_debut < end and self.timecode_fin > start:
                return [self._create_occurrence(self.timecode_debut)]
            else:
                return []

    def _occurrences_after_generator(self, after=None):
        """
        returns a generator that produces unpresisted occurrences after the
        datetime ``after``. (Optionally) This generator will return up to
        ``max_occurrences`` occurrences or has reached ``self.end_recurring_period``, whichever is smallest.
        """

        tzinfo = timezone.utc
        if after is None:
            after = timezone.now()
        elif not timezone.is_naive(after):
            tzinfo = after.tzinfo
        rule = self.get_rrule_object(tzinfo)
        if rule is None:
            if self.timecode_fin > after:
                yield self._create_occurrence(self.timecode_debut, self.timecode_fin)
            return
        date_iter = iter(rule)
        difference = self.timecode_fin - self.timecode_debut
        loop_counter = 0
        for o_start in date_iter:
            o_start = tzinfo.localize(o_start)
            o_end = o_start + difference
            if o_end > after:
                yield self._create_occurrence(o_start, o_end)

            loop_counter += 1

    def occurrences_after(self, after=None, max_occurrences=None):
        """
        returns a generator that produces occurrences after the datetime
        ``after``.  Includes all of the persisted Occurrences. (Optionally) This generator will return up to
        ``max_occurrences`` occurrences or has reached ``self.end_recurring_period``, whichever is smallest.
        """
        if after is None:
            after = timezone.now()
        occ_replacer = OccurrenceReplacer(self.occurrence_set.all())
        generator = self._occurrences_after_generator(after)
        trickies = list(
            self.occurrence_set.filter(
                original_start__lte=after, start__gte=after
            ).order_by('timecode_debut')
        )
        for index, nxt in enumerate(generator):
            if max_occurrences and index > max_occurrences - 1:
                break
            if len(trickies) > 0 and (nxt is None or nxt.timecode_debut > trickies[0].timecode_debut):
                yield trickies.pop(0)
            yield occ_replacer.get_occurrence(nxt)

    @property
    def event_start_params(self):
        start = self.timecode_debut
        params = {
            "byyearday": start.timetuple().tm_yday,
            "bymonth": start.month,
            "bymonthday": start.day,
            "byweekno": start.isocalendar()[1],
            "byweekday": start.weekday(),
            "byhour": start.hour,
            "byminute": start.minute,
            "bysecond": start.second,
        }
        return params

    @property
    def event_rule_params(self):
        return self.rule.get_params()

    def _event_params(self):
        freq_order = freq_dict_order[self.rule.frequency]
        rule_params = self.event_rule_params
        start_params = self.event_start_params
        event_params = {}

        if len(rule_params) == 0:
            return event_params

        for param in rule_params:
            # start date influences rule params
            if (
                param in param_dict_order
                and param_dict_order[param] > freq_order
                and param in start_params
            ):
                sp = start_params[param]
                if sp == rule_params[param] or (
                    hasattr(rule_params[param],
                            "__iter__") and sp in rule_params[param]
                ):
                    event_params[param] = [sp]
                else:
                    event_params[param] = rule_params[param]
            else:
                event_params[param] = rule_params[param]

        return event_params

    @property
    def event_params(self):
        event_params = self._event_params()
        start = self.effective_start
        empty = False
        if not start:
            empty = True
        elif self.end_recurring_period and start > self.end_recurring_period:
            empty = True
        return event_params, empty

    @property
    def effective_start(self):
        if self.pk and self.end_recurring_period:
            occ_generator = self._occurrences_after_generator(
                self.timecode_debut)
            try:
                return next(occ_generator).timecode_debut
            except StopIteration:
                pass
        elif self.pk:
            return self.timecode_debut
        return None

    @property
    def effective_end(self):
        if self.pk and self.end_recurring_period:
            params, empty = self.event_params
            if empty or not self.effective_start:
                return None
            elif self.end_recurring_period:
                occ = None
                occ_generator = self._occurrences_after_generator(
                    self.timecode_debut)
                for occ in occ_generator:
                    pass
                return occ.end
        elif self.pk:
            return datetime.datetime.max
        return None


class SeanceManager(EventManager):
    def get_for_object(self, content_object, distinction="", inherit=True):
        return SeanceRelation.objects.get_events_for_object(
            content_object, distinction, inherit
        )


class SeanceRelationManager(EventRelationManager):
    def get_events_for_object(self, content_object, distinction="", inherit=True):
        ct = ContentType.objects.get_for_model(type(content_object))
        if distinction:
            dist_q = Q(eventrelation__distinction=distinction)
            cal_dist_q = Q(calendar__calendarrelation__distinction=distinction)
        else:
            dist_q = Q()
            cal_dist_q = Q()
        if inherit:
            inherit_q = Q(
                cal_dist_q,
                calendar__calendarrelation__content_type=ct,
                calendar__calendarrelation__object_id=content_object.id,
                calendar__calendarrelation__inheritable=True,
            )
        else:
            inherit_q = Q()
        event_q = Q(
            dist_q,
            eventrelation__content_type=ct,
            eventrelation__object_id=content_object.id,
        )
        return Seance.objects.filter(inherit_q | event_q)

    def create_relation(self, event, content_object, distinction=""):
        """
        Creates a relation between event and content_object.
        See EventRelation for help on distinction.
        """
        return SeanceRelation.objects.create(
            event=event, distinction=distinction, content_object=content_object
        )


class SeanceRelation(EventRelation):
    seance = models.ForeignKey(
        Seance, on_delete=models.CASCADE, verbose_name=("Séance"))

    objects = SeanceRelationManager()

    class Meta:
        verbose_name = ("Séance relation")

    def __str__(self):
        return "{}({})-{}".format(
            self.seance.title, self.distinction, self.content_object
        )

# à customiser selon mais nécessaires pour l'obtention du calendrier


class SeanceOccurence(Occurrence):
    seance = models.ForeignKey(
        Seance, on_delete=models.CASCADE, verbose_name=("Séance"))
    debut = models.DateTimeField(("Début de l'occurrence"), db_index=True)
    fin = models.DateTimeField(("Fin"), db_index=True)

    class Meta:
        verbose_name = ("Occurence")


class SeanceCalendrierManager(CalendarManager):
    def get_or_create_calendar_for_object(self, obj, distinction="", name=None):
        try:
            return self.get_calendar_for_object(obj, distinction)
        except SeanceCalendrier.DoesNotExist:
            if name is None:
                calendar = self.model(name=str(obj))
            else:
                calendar = self.model(name=name)
            calendar.slug = slugify(calendar.name)
            calendar.save()
            calendar.create_relation(obj, distinction)
            return calendar


class SeanceCalendrier(Calendar):
    seances = SeanceCalendrierManager()

    def occurrences_after(self, date=None):
        return SeanceListManager(self.events.all()).occurrences_after(date)

    class Meta:
        verbose_name = 'Calendrier'
